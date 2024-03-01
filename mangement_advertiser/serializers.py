from rest_framework import serializers
from .models import Ad, Advertiser

class CreateAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'img_url', 'link', 'advertiser']

class AdveriserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    advertiser = Advertiser()
    class Meta:
        model = Ad
        fields = '__all__'