from django.db import models


class Category(models.Model):
    Status = (
        ('True','Evet'),
        ('False','Hayir'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=Status)
    slug = models.SlugField()
    parent = models.ForeignKey('self' , blank=True , related_name='children' , on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
