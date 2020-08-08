from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
import datetime
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.conf import  settings


def year_choices():
    return [(r, r) for r in range(1900, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class Category(MPTTModel):
    Status = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=Status)
    slug = models.SlugField(null=False,unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})


class Car(models.Model):
    Status = (
        ('True', 'YES'),
        ('False', 'NO'),
    )
    TRANSMISSION = (
        ('manual', 'MANUAL'),
        ('automatic', ' AUTOMATIC'),
    )
    STATE = (
        ('new', 'NEW'),
        ('used', 'USED'),
    )
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(null=False,unique=True,blank=True)
    status = models.CharField(max_length=10, choices=Status ,default='NO')
    photo = models.ImageField(blank=True, upload_to='images/',default='images/default_car.jpg')
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year_of_production = models.IntegerField('year', choices=year_choices(), default=current_year())
    engine_capacity = models.IntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION)
    km = models.IntegerField()
    state = models.CharField(max_length=10, choices=STATE)
    price = models.FloatField(max_length=30)
    fuel_type = models.CharField(max_length=30)
    details = RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.photo.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('VehicleDetailView', kwargs={'slug':self.slug})


class Image(models.Model):
    cars = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=30,blank=True)
    image = models.ImageField(blank=True, upload_to='images/',null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Comment(models.Model):
    STATUS = (
        ('New',"NEW"),
        ('True', 'YES'),
        ('False', "NO"),
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50,blank=True)
    comment = models.TextField(max_length=250,blank=True)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True,max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Brand(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField( upload_to='images/brands',)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
