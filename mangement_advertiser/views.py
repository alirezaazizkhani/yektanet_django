from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView

from .models import Ad, Advertiser, Click, View
from .serializers import AdSerializer, CreateAdSerializer, AdveriserSerializer

class ListAdvertiserView(ListCreateAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdveriserSerializer

    def get(self, request, *args, **kwargs):
        advertiseres = self.get_queryset()
        serializer = AdveriserSerializer(advertiseres, many=True)
        data = []
        for advertiser in serializer.data:
            ads = Ad.objects.filter(advertiser_id__id = advertiser['id'] )
            ads_serializer = AdSerializer(ads, many=True)
            advertiser['ads'] = ads_serializer.data
            data.append(advertiser)
        return Response(data)


class DetailAdvertiserView(RetrieveUpdateDestroyAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdveriserSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try :
            advertiser = Advertiser.objects.get(pk=pk)
            serializer = self.serializer_class(advertiser)
            data = []
            data.append(serializer.data)
            data[0]['ads'] = AdSerializer(Ad.objects.filter(advertiser_id__id = serializer.data['id']), many=True).data
            return Response(data)
        except:
            return Response({"errors": "Not found"})

class ListAdView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    def get(self, request, *args, **kwargs):
        ads = self.get_queryset()
        serializer = self.serializer_class(ads, many=True)
        data = []
        for ad in serializer.data:
            advertiser = Advertiser.objects.filter(id=ad['advertiser'])
            advertiser_serializer = AdveriserSerializer(advertiser, many=True)
            ad['advertiser'] = advertiser_serializer.data
            data.append(ad)
        return Response(data)        

class CreateAdView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = CreateAdSerializer

class DetailAdView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = CreateAdSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            ad = Ad.objects.get(pk=pk)
            serializer = self.serializer_class(ad)
            data = []
            data.append(serializer.data)
            data[0]['advertiser'] = AdveriserSerializer(Advertiser.objects.filter(id = serializer.data['advertiser']), many =True).data
            return Response(data)
        except:
            return Response({"errors": "Not found"})


class AdView(APIView):
    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        data = []
        for ad in serializer.data:
            advertiser = Advertiser.objects.filter(id=ad['advertiser'])
            advertiser_serializer = AdveriserSerializer(advertiser, many=True)
            ad['advertiser'] = advertiser_serializer.data
            data.append(ad)
        return Response(serializer.data)


class AdReportsView(TemplateView):
    template_name = 'mangement_advertiser/advertising_report.html'
    def get(self, request):
        clicks_by_hour = Click.objects.values('click_time__hour').annotate(click_count=Count('id')).order_by('click_time__hour')
        views_by_hour = View.objects.values('view_time__hour').annotate(view_count=Count('id')).order_by('view_time__hour')
        
        total_clicks = Click.objects.count()
        total_views = View.objects.count()
        click_to_view_ratio_total = total_clicks / total_views if total_views > 0 else 0
        
        views_by_h = View.objects.values('view_time__hour').annotate(view_count=Count('id'))
        click_to_view_ratio_by_hour = []
        for view in views_by_h:
            click_by_h = Click.objects.values('click_time__hour').filter(click_time__hour=view['view_time__hour']).annotate(click_count=Count('id'))
            click_to_view_ratio_by_hour.append({"time": view['view_time__hour'],
                                                "ratio": click_by_h[0]['click_count']/view['view_count']
                                                })

        average_diff = []
        clicks = Click.objects.values('user_ip', 'click_time', 'ad_id')
        for click in clicks:
            last_view = View.objects.values('user_ip', 'view_time', 'ad_id').filter(user_ip=click['user_ip'], view_time__lt= click['click_time'], ad_id = click['ad_id']).order_by('-view_time')[0]
            average_diff.append(int(click['click_time'].strftime("%Y%m%d%H%M%S")) - int(last_view['view_time'].strftime("%Y%m%d%H%M%S")))
        average_diff = sum(average_diff)/len(average_diff)

        context = {
            'clicks_by_hour': clicks_by_hour,
            'views_by_hour': views_by_hour,
            'click_to_view_ratio': click_to_view_ratio_total,
            'click_to_view_ratio_by_hour' : click_to_view_ratio_by_hour ,
            "average_difference_between_view_and_click_time": average_diff 
        }

        return render(request, self.template_name, {"context":context})