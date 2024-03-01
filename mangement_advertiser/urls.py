from django.urls import path
from . import views

urlpatterns = [
    path('advertiseres/', views.AdvertiserView.as_view({'get': 'list', 'post':'create'})),
    path('advertiseres/<int:pk>/', views.AdvertiserView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put':'update'})),
    path('ads/', views.AdView.as_view({'get': 'list', 'post':'create'})),
    path('ads/<int:pk>/', views.AdView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put':'update'})),
    path('report/', views.AdReportsView.as_view(), name='report'),
]