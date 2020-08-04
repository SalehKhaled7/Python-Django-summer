from django.urls import path
from .views import (VehicleListView ,
                    VehicleDetailView,
                    VehicleCreateView)
from user import views
app_name='cars'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    path('ads/', VehicleListView.as_view(), name='VehicleListView'),
    path('ads/<slug>/', VehicleDetailView.as_view(), name='VehicleDetailView'),
    path('new/ad/', VehicleCreateView.as_view(), name='VehicleCreateView'),
]