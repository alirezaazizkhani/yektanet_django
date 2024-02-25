from django import forms

from .models import Ad

class InputAd(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [ "Title", "imgUrl", "Link", "advertiser"]

