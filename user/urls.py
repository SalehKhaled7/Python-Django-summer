from django.urls import path
from .views import  VehicleDetailView
from user import views
app_name='cars'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    #path('ads/', VehicleListView.as_view(), name='VehicleListView'),
    path('ads/', views.user_ads, name='user_ads'),
    path('ads/<str:pk>/', VehicleDetailView.as_view(), name='VehicleDetailView'),
    #path('new/add/', VehicleCreateView.as_view(), name='VehicleCreateView'),
    path('new/ad/', views.user_new_ad, name='user_new_ad'),
    path('ads/<str:pk>/update/', views.user_ad_update, name='user_ad_update'),
    path('ads/<str:pk>/delete/', views.user_ad_delete, name='user_ad_delete'),
]