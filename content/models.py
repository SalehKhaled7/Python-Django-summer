from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(MPTTModel):
    STATUS = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30,unique=True)
    link = models.CharField(max_length=255,blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
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


class Content(models.Model):
    STATUS = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    TYPE = (
        ('menu','menu'),
        ('event','event'),
        ('notification','notification'),
        ('news','news'),
        ('ad','ad'),
    )
    menu = models.OneToOneField(Menu, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=TYPE)
    status = models.CharField(max_length=10, choices=STATUS)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    detail =RichTextUploadingField()
    slug = models.SlugField(null=False,unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})

class CImage(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=30,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
