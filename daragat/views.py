from django.shortcuts import render
from . models import daragat
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required
def all_darajat(request):
    all_darajat = daragat.objects.all()
    return render(request, 'darajat/all_shahada.html', {'shahada':all_darajat})
