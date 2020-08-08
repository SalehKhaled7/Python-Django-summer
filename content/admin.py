from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from content.models import Content, Menu, CImage

class ContentImageInline(admin.TabularInline):
    model = CImage
    extra = 3


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','type','status','create_at']
    list_filter =['status','type']
    inlines = [ContentImageInline]
    prepopulated_fields = {'slug':('title',)}


class MenuAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions','indented_title','status')
    list_filter = ['status']


admin.site.register(Menu,MenuAdmin)
admin.site.register(Content,ContentAdmin)

