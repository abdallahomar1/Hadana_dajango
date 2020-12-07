import django_filters
from .models import daragat

class filter(django_filters.FilterSet):
    #name_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = daragat
        fields = ['kind', 'name_name', 'clas']
