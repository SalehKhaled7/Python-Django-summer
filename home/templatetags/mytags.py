from django import template

from cars.models import Category
from content.models import Menu, Content

register =template.Library()

@register.simple_tag
def category_list():
    return Category.objects.all()

@register.simple_tag
def menu_list():
    return Menu.objects.all()

@register.simple_tag
def home_top_msg1():
    return Content.objects.get(slug='top-msg-1')

@register.simple_tag
def home_top_msg2():
    return Content.objects.get(slug='top-msg-2')



