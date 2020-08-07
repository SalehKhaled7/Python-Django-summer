from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea


class Setting(models.Model):
    Status = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(blank=True, max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    fax = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    smtp_server = models.CharField(blank=True, max_length=20)
    smtp_email = models.CharField(blank=True, max_length=20)
    smtp_password = models.CharField(blank=True, max_length=15)
    smtp_port = models.CharField(blank=True, max_length=10)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    about_us = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=Status)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    send_to = models.ForeignKey(User,default=User.objects.get(pk=1).id,on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message', ]
        widgets = {
            'name': TextInput(attrs={'class': 'input'}),
            'email': TextInput(attrs={'class': 'input'}),
            'subject': TextInput(attrs={'class': 'input'}),
            'message': Textarea(attrs={'class': 'input', 'rows': '5'}),
        }

class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    question_num=models.IntegerField(default=0)
    question = models.CharField(max_length=250)
    answer = RichTextUploadingField()
    status=models.CharField(max_length=15,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
