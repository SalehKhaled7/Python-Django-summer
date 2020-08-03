from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default='05---------')
    address = models.CharField(blank=True, max_length=150,default='default_address')
    city = models.CharField(max_length=20,default='default_city')
    country = models.CharField(max_length=20,default='default_country')
    image = models.ImageField(upload_to='images/users/',default='images/users/default_user.jpg')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return '[' + self.user.username + ']' + self.user.first_name + ' ' + self.user.last_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','city','country','image']