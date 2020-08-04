from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from cars.models import Category, Car
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile
from django.views.generic import ListView, DetailView, CreateView
from .forms import CarModelForm



def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile,}
    return render(request,'user_profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
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
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form,'category': category
                       })



class VehicleListView(ListView):
    template_name = 'user_ads.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return Car.objects.order_by('-create_at')

    def get_context_data(self, **kwargs):
        context = super(VehicleListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class VehicleDetailView(DetailView):
    model = Car
    template_name = 'user_ads_details.html'

    def get_context_data(self, **kwargs):
        context = super(VehicleDetailView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class VehicleCreateView(LoginRequiredMixin,CreateView):
    template_name = 'car_form.html'
    form_class = CarModelForm
    queryset = Car.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VehicleCreateView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context






