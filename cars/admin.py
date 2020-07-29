from django.contrib import admin
from cars.models import Category, car, Image


class CarImagesInLine(admin.TabularInline):
    model = Image
    extra = 4


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class CarAdmin(admin.ModelAdmin):
    list_display = ['title','model','image_tag','color','status']
    list_filter = ['status']
    inlines = [CarImagesInLine]
    readonly_fields = ('image_tag',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(car, CarAdmin)
admin.site.register(Image, ImageAdmin)
