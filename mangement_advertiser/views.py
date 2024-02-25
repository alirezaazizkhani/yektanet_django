from django.http import Http404
from django.shortcuts import render, redirect

from .models import Ad, Advertiser
from .forms import InputAd

def main(request):
    advertiseres = Advertiser.objects.all()
    data = []
    for advertiser in advertiseres:
        data.append({
            'advertiser': advertiser,
            'ads': Ad.objects.filter(advertiser__ID = advertiser.ID)
        })
    return render(request, 'mangement_advertiser/main.html', {"data": data})

def ad_handler(request, ad_id):
    try : 
        ad = Ad.objects.get(ID=ad_id)
    except Ad.DoesNotExist:
        raise Http404("Ad does not exist")
    ad.Clicks += 1
    ad.Views += 1
    advertiser = ad.advertiser
    advertiser.Clicks += 1
    advertiser.Views += 1
    ad.save()
    advertiser.save()
    return redirect(ad.Link)


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