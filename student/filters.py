import django_filters
from .models import Student, Absence

class filter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['imag', 'Time_add']

class mybfilter(django_filters.FilterSet):
    time = django_filters.DateTimeFilter()
    name_student = django_filters.CharFilter(lookup_expr='icontains')
    Reason = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Absence
        fields = '__all__'
