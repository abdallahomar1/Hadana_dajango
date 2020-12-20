from django.shortcuts import render
from daragat.filters import filter
from . models import daragat
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
# Create your views here.
#@login_required
def all_darajat(request):
    all_darajat = daragat.objects.all()
    myfilter = filter(request.GET, queryset=all_darajat)
    all_darajat = myfilter.qs
    return render(request, 'darajat/all_shahada.html', {'shahada':all_darajat, 'filter':myfilter})

def my(request, id):
    shahada_one = daragat.objects.get(id=id)
    context = {
        'shahada':shahada_one
    }
    return render(request, 'darajat/shahada.html', context)

def all_shah(request):
    all_darajat = daragat.objects.all()
    return render(request, 'darajat/all_daragat.html', {'shahada':all_darajat})
