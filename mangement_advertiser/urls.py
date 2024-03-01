from django.urls import path
from . import views

urlpatterns = [
    path('advertiseres/', views.ListAdvertiserView.as_view()),
    path('advertiseres/<int:pk>/', views.DetailAdvertiserView.as_view()),
    path('ads/', views.ListAdView.as_view()),
    path('ads/create/', views.CreateAdView.as_view()),
    path('ads/<int:pk>/', views.DetailAdView.as_view()),
    path('report/', views.AdReportsView.as_view(), name='report'),
]