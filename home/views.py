from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting, ContactForm, ContactFormMessage


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
    form = ContactForm()
    context = {'setting': setting,'form':form}
    return render(request,'contact_us.html',context)
