from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting

# Create your views here.


def index(request):
    setting = Setting.objects.get()
    context = {'setting': setting , 'page':'index'}
    return render(request,'index.html',context)


def about_us(request):
    setting = Setting.objects.get()
    context = {'setting': setting,'page':'about_us'}
    return render(request,'about_us.html',context)


def contact(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request,'contact_us.html',context)
