from typing import Any
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView, FormView
from django.shortcuts import get_object_or_404


from .models import Ad, Advertiser, Click, View
from .forms import InputAd

class MainView(TemplateView):
    template_name = 'mangement_advertiser/main.html'
    def get_context_data(self, **kwargs):
        context = context = super().get_context_data(**kwargs)
        advertiseres = Advertiser.objects.all()
        context['data'] = [{
            'advertiser': advertiser,
            'ads': Ad.objects.filter(advertiser_id = advertiser.id)
        }for advertiser in advertiseres]
        return context


class AdHandlerView(RedirectView):

    def get(self, request, ad_id):
        ad = get_object_or_404(Ad, id=ad_id)
        Click(ad_id = ad, user_ip = request.ip).save()
        View(ad_id = ad, user_ip = request.ip).save()
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
