from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import get_object_or_404

from .models import Ad, Advertiser, Click, View
from .forms import InputAd


class MainView(TemplateView):
    template_name = 'mangement_advertiser/main.html'
    def get(self, request):
        advertiseres = Advertiser.objects.all()
        for advertiser in advertiseres:
            ads = Ad.objects.filter(advertiser_id = advertiser.id)
            for ad in ads:
                View(ad_id = ad, user_ip = request.ip ).save()
        context = {
            "data":[{
            'advertiser': advertiser,
            'ads': Ad.objects.filter(advertiser_id = advertiser.id)
        }for advertiser in advertiseres]}
        return render(request, self.template_name, context)

class AdHandlerView(RedirectView):
    def get(self, request, ad_id):
        ad = get_object_or_404(Ad, id=ad_id)
        Click(ad_id = ad, user_ip = request.ip).save()
        return redirect(ad.link)


class AddAdsView(TemplateView):
    template_name = "mangement_advertiser/add_ad.html"
    
    def get(self, request):
        form = InputAd()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InputAd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  
        else:
            return render(request, self.template_name, {'form': form})

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