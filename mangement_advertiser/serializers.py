from rest_framework import serializers
from .models import Ad, Advertiser


class AdveriserSerializer(serializers.ModelSerializer):
    ads = serializers.SerializerMethodField()
    class Meta:
        model = Advertiser
        fields = ['id','name','ads']

    def get_ads(self, obj):
        result  = Advertiser.objects.filter(ad=obj.id).values('ad__id','ad__title')
        return result

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'img_url', 'link', 'advertiser']
    

