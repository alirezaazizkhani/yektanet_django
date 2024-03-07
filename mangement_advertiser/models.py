from django.db import models
import datetime


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

class Click(models.Model):
    id = models.IntegerField(primary_key=True)
    ad_id = models.ForeignKey('Ad', on_delete=models.PROTECT)
    user_ip = models.GenericIPAddressField()
    click_time = models.DateTimeField(default=datetime.datetime.now)

class View(models.Model):
    id = models.IntegerField(primary_key=True)
    ad_id = models.ForeignKey('Ad', on_delete=models.PROTECT)
    user_ip = models.GenericIPAddressField()
    view_time = models.DateTimeField(default=datetime.datetime.now)

class Saver(models.Model):
    count = models.IntegerField()
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.count