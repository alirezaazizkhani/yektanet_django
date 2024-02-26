from django.db import models

class Advertiser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Ad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    advertiser = models.ForeignKey('Advertiser', on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)    
    
    def __str__(self):
        return self.title
    
    def inc_clicks(self):
        self.clicks += 1
        self.advertiser_id.clicks += 1
    
    def inc_views(self):
        self.views += 1
        self.advertiser.views += 1

class Click(models.Model):
    id = models.IntegerField(primary_key=True)
    ad_id = models.ForeignKey('Ad', on_delete=models.PROTECT)
    user_ip = models.IntegerField()
    click_time = models.DateTimeField(auto_now=True)

class View(models.Model):
    id = models.IntegerField(primary_key=True)
    ad_id = models.ForeignKey('Ad', on_delete=models.PROTECT)
    user_ip = models.IntegerField()
    click_time = models.DateTimeField(auto_now=True)