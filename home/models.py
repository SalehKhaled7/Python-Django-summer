from django.db import models

# Create your models here.


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
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=15)
    smtpport = models.CharField(blank=True, max_length=10)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField(blank=True)
    references = models.CharField(blank=True, max_length=50)
    status = models.CharField(max_length=10, choices=Status)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


