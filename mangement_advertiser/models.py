from django.db import models




class Advertiser(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=25)
    Clicks = models.IntegerField(default=0)
    Views = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

class Ad(models.Model):
    ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=255)
    Link = models.CharField(max_length=255)
    Clicks = models.IntegerField(default=0)
    Views = models.IntegerField(default=0)
    Advertiser = models.ForeignKey('Advertiser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Title