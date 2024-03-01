from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('advertiseres/', views.AdvertiserView.as_view({'get': 'list', 'post':'create'})),
    path('advertiseres/<int:pk>/', views.AdvertiserView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put':'update'})),
    path('ads/', views.AdView.as_view({'get': 'list', 'post':'create'})),
    path('ads/<int:pk>/', views.AdView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put':'update'})),
    path('report/', views.AdReportsView.as_view(), name='report'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]