from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view() , name="main"),
    path('ad/<int:ad_id>/', views.AdHandlerView.as_view(), name="ad_handler"),
    path('add_ads/', views.AddAdsView.as_view(), name="add_ads"),
]