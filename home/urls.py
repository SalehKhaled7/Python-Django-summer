from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('buy/', views.buy_a_car, name='buy_a_car'),
]
