from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('aboutus/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('buy/', views.buy_a_car, name='buy_a_car'),
    path('faq/', views.faq, name='faq'),
    path('menu/<int:id>', views.menu, name='menu'),
    path('content/<int:id>/<slug:slug>/', views.contentDetail, name='contentDetail'),
]
