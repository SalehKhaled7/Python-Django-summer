from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting

# Create your views here.


def index(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request,'index.html',context)

