from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from cars.models import Category, Car, Image, Comment


class CarImagesInLine(admin.TabularInline):
    model = Image
    extra = 4


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(qs,Car, 'category','products_cumulative_count', cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,Car,'category','products_count',cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class CarAdmin(admin.ModelAdmin):
    list_display = ['title','model','image_tag','status']
    list_filter = ['status']
    inlines = [CarImagesInLine]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    readonly_fields = ('image_tag',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'car', 'user', 'status']
    list_filter = ['status']


admin.site.register(Category,CategoryAdmin2)
admin.site.register(Car, CarAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment,CommentAdmin)
