import django_filters
from .models import Student, Absence
from django import forms
class filter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['imag', 'Time_add', 'phone_father', 'numer']

class mybfilter(django_filters.FilterSet):
    #time = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    Reason = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Absence
        fields = '__all__'
