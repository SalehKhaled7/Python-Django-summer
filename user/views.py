from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from cars.models import Category, Car, Image
from user.forms import UserUpdateForm, ProfileUpdateForm, AdImageForm
from user.models import UserProfile
from django.views.generic import DetailView
from .forms import CarModelForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile, }
    return render(request, 'user_profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(
            instance=request.user.userprofile)  # "userprofile" model -> OneToOneField relations with user
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form, 'category': category})


class VehicleDetailView(DetailView):
    model = Car
    template_name = 'user_ads_details.html'

    def get_context_data(self, **kwargs):
        context = super(VehicleDetailView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


def user_new_ad(request):
    image_form_set = formset_factory(AdImageForm, extra=4)
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES)
        formset = image_form_set(request.POST or None, request.FILES)
        if form.is_valid() and formset.is_valid():
            ad = form.save(commit=False)
            ad.owner = request.user
            ad.save()
            for f in formset:
                try:
                    img = Image(cars=ad, image=f.cleaned_data['image'], title=f.cleaned_data['title'])
                    img.save()
                except Exception as e:
                    break
            return HttpResponseRedirect('/user/ads')
    else:
        form = CarModelForm()
        formset = image_form_set()
    category = Category.objects.all()
    context = {'form': form,
               'category': category,
               'formset': formset, }
    return render(request, 'new_ad.html', context)


def user_ads(request):
    ads = Car.objects.filter(owner=request.user)
    category = Category.objects.all()
    context = {'ads': ads,
               'category': category, }
    return render(request, 'user_ads.html', context)


def user_ad_update(request, pk):
    ad = Car.objects.get(id=pk)
    form = CarModelForm(instance=ad)
    ad_images_form = AdImageForm
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES, instance=ad)
        ad_images_form = AdImageForm(request.POST, request.FILES)
        if form.is_valid() and ad_images_form.is_valid():
            form.save()
            ad_images_form.save()
            return HttpResponseRedirect('/user/ads/' + pk)
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
        'ad_images_form': ad_images_form,
    }
    return render(request, 'user_ad_update.html', context)


def user_ad_delete(request, pk):
    ad = Car.objects.get(id=pk)

    if request.method == "POST":
        ad.delete()
        return HttpResponseRedirect('/user/ads/')
    category = Category.objects.all()
    context = {'category': category,
               'ad': ad, }
    return render(request, 'user_ad_delete.html', context)
