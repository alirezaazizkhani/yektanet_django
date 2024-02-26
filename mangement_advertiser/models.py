from django.db import models

class Advertiser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    advertiser = models.ForeignKey('Advertiser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def inc_clicks(self):
        self.clicks += 1
        self.advertiser_id.clicks += 1
    
    def inc_views(self):
        self.views += 1
        self.advertiser.views += 1