from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name='api-overview'),
  path('charginginfo-list/', views.charginginfoList, name='charginginfo-list'),
  path('charginginfo-detail/<str:pk>/', views.charginginfoDetail, name='charginginfo-detail'),
  path('charginginfo-create/', views.charginginfoCreate, name='charginginfo-create'),
  path('charginginfo-update/<str:pk>/', views.charginginfoUpdate, name='charginginfo-update'),
  path('charginginfo-delete/<str:pk>/', views.charginginfoDelete, name='charginginfo-delete'),
]