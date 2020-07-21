from django.contrib import admin
from cars.models import Category, car, Image


class CarImagesInLine(admin.TabularInline):
    model = Image
    extra = 4


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class CarAdmin(admin.ModelAdmin):
    list_display = ['title','model','color','status']
    list_filter = ['status']
    inlines = [CarImagesInLine]


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(car, CarAdmin)
admin.site.register(Image, ImageAdmin)
