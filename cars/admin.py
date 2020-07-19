from django.contrib import admin
from cars.models import Category, car


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class CarAdmin(admin.ModelAdmin):
    list_display = ['title','model','color','status']
    list_filter = ['status']


admin.site.register(Category, CategoryAdmin)
admin.site.register(car, CarAdmin)
