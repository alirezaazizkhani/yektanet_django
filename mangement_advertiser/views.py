from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Ad, Advertiser, Click, View, Saver
from .serializers import AdSerializer, AdveriserSerializer

class AdvertiserView(ModelViewSet):
    serializer_class = AdveriserSerializer
    queryset = Advertiser.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AdView(ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]        


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