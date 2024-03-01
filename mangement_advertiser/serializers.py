from rest_framework import serializers
from .models import Ad, Advertiser

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class AdveriserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'

