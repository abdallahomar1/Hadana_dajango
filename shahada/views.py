from django.shortcuts import render
from daragat.models import daragat
# Create your views here.

def my(request, id):
    shahada_one = daragat.objects.get(id=id)
    context = {
        'shahada':shahada_one
    }
    return render(request, 'darajat/shahada.html', context)
