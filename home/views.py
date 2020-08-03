import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from cars.models import Car, Category, Image
from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactFormMessage
from user.forms import SignUpForm
from user.models import UserProfile


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


def car_details(request,id,slug):
    setting = Setting.objects.get()
    car = Car.objects.get(pk=id)
    images = Image.objects.filter(cars_id=id)
    category = Category.objects.all()
    context = {'setting': setting,'category': category,'car': car,'images': images,}
    return render(request,'car_details.html',context)


def car_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            cars = Car.objects.filter(title__icontains=query)
            context = {'cars': cars,
                       'category': category,}
            return render(request, 'car_search.html', context)
    return HttpResponseRedirect('/')


def car_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        cars = Car.objects.filter(title__icontains=q)
        results = []
        for rs in cars:
            car_json = {}
            car_json = rs.title
            results.append(car_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/home")
    # Redirect to a success page.


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "wrong user name or password please try again")
            return HttpResponseRedirect("/login")

    category = Category.objects.all()
    context = {'category': category,}
    return render(request,'login.html', context)


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request,user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.save()
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form, }
    return render(request, 'signup.html', context)




