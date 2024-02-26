from django.http import Http404
from django.shortcuts import render, redirect

from .models import Ad, Advertiser
from .forms import InputAd

def main(request):
    advertiseres = Advertiser.objects.all()
    data = [{
            'advertiser': advertiser,
            'ads': Ad.objects.filter(advertiser_id = advertiser.id)
        }for advertiser in advertiseres]
    return render(request, 'mangement_advertiser/main.html', {"data": data})

def ad_handler(request, ad_id):
    try : 
        ad = Ad.objects.get(id=ad_id)
    except Ad.DoesNotExist:
        raise Http404("Ad does not exist")
    ad.inc_clicks()
    ad.inc_views()
    ad.save()
    ad.advertiser.save()
    return redirect(ad.link)


def add_ads(request):
    if(request.method == 'POST'):
        form = InputAd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(main)
    else:        
        context = {
            'form': InputAd()
        }
        return render(request, "mangement_advertiser/add_ad.html", context)