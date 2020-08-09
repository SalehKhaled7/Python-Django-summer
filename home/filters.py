import django_filters
from django.forms import TextInput

from cars.models import *


class VehicleFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt',label="Min price")
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt',label="Max price")
    manufacturer = django_filters.CharFilter(label="Brand")


    class Meta:
        model = Car
        fields = ['category', 'manufacturer', 'year_of_production']

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }}
