from django import template

from cars.models import Category
from content.models import Menu

register =template.Library()

@register.simple_tag
def category_list():
    return Category.objects.all()

@register.simple_tag
def menu_list():
    return Menu.objects.all()
