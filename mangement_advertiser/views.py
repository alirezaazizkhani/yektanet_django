from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

from .models import Ad, Advertiser


def main(request):
    advertiseres = Advertiser.objects.all()
    data = []
    for advertiser in advertiseres:
        data.append({
            'advertiser': advertiser,
            'ads': Ad.objects.filter(advertiser__ID = advertiser.ID)
        })
    return render(request, 'mangement_advertiser/main.html', {"data": data})
