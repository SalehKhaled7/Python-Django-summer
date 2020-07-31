from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from cars.models import Car, Category
from home.models import Setting, ContactForm, ContactFormMessage


# Create your views here.


def index(request):
    setting = Setting.objects.get()
    slider_data = Car.objects.all()[:5]
    category = Category.objects.all()
    week_deals = Car.objects.all()[:5]
    best_sell = Car.objects.all().order_by('?')[:5]
    context = {'setting': setting,
               'page':'index',
               'slider_data':slider_data,
               'category': category,
               'week_deals': week_deals,
               'best_sell': best_sell,
               }
    return render(request,'index.html',context)


def about_us(request):
    setting = Setting.objects.get()
    category = Category.objects.all()
    context = {'setting': setting,'page':'about_us','category': category,}
    return render(request,'about_us.html',context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "the message has been send successfully ")
            return HttpResponseRedirect("/contact")

    setting = Setting.objects.get()
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting,'form':form,'category': category,}
    return render(request,'contact_us.html',context)


def buy_a_car(request, id, slug):
    setting = Setting.objects.get()
    cars = Car.objects.filter(category_id=id)
    category = Category.objects.all()
    context = {'setting': setting,'category': category,'cars': cars,}
    return render(request,'buy.html',context)
