from django.urls import path
from . import views

urlpatterns = [
    path('', views.main , name="main"),
    path('ad/<int:ad_id>/', views.ad_handler, name="ad_handler"),
    path('add_ads/', views.add_ads, name="add_ads"),
]