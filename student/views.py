from django.shortcuts import render
from student.models import Absence
from daragat.models import daragat
from  . models import Student, classstudent, masrofat, Category_masrof , mawad, Absence, hafela as buses, rateb
from django.db.models import Sum
from .filters import filter, mybfilter
from django.contrib.auth.decorators import login_required
from daragat.models import daragat
#from . forms import Absence
from . import models
# Create your views here.
#@login_required
def all_student(request):
    student_list = Student.objects.all()
    myfilter = filter(request.GET, queryset=student_list)
    student_list = myfilter.qs
    context = {'students':student_list, 'myfilter': myfilter}
    return render(request, 'student/all_students.html', context)


def student_one(request, id):
    student_one = Student.objects.get(id=id)
    student_img = Student.objects.all()
    
    context = {'onestudent':student_one, 'imagestudent':student_img}
    return render(request, 'student/student.html', context)

def rebh(request):
    paid = Student.objects.aggregate(Sum('amount_paid'))
    masrof = masrofat.objects.aggregate(Sum('price_masrofat'))
    bake = Student.objects.aggregate(Sum('Remaining_amount'))
    bus = buses.objects.aggregate(Sum('bus_price'))
    new = bus['bus_price__sum'] * 3
    bakes = bake['Remaining_amount__sum'] * 1
    masrofs = masrof['price_masrofat__sum'] * 1
    paids = paid['amount_paid__sum'] * 1
    myrateb = rateb.objects.aggregate(Sum('yuor_rateb'))
    ratebs = myrateb['yuor_rateb__sum'] * 3
    remain = paid['amount_paid__sum'] - masrof['price_masrofat__sum']
    rebh = remain - new - ratebs
    return render(request, 'student/hasel.html', {'hasel':rebh, 'ward':paids, 'sadr':masrofs, 'bus':new, 'bake':bakes, 'reteb':ratebs})

def employees(request):
        employees = masrofat.objects.all()
        context = {'employees':employees}
        return render(request, 'student/employees.html', context)

def employees_one(request, id):
    employees_one = masrofat.objects.get(id=id)
    context = {'one_masrof': employees_one}
    return render(request, 'student/one_employees.html', context)

def alkeyab(request):
    khaeb = Absence.objects.order_by('-time')
    myfilter = mybfilter(request.GET, queryset=khaeb)
    khaeb = myfilter.qs
    #myv = Absence.the_Absence()
    context = {
        'all_keyab':khaeb, 'kaeb_filter':myfilter
    }
    return render(request, 'student/khaeb.html', context)

def myfun(request):
    khaebs = Absence.objects.order_by('-time')
    return render(request, 'student/kjh.html', {'myf':khaebs})

def my(request, id):
    shahada_one = daragat.objects.get(id=id)
    context = {
        'shahada':shahada_one
    }
    return render(request, 'darajat/shahada.html', context)
# def register(request):
#     form=Absence(request.POST or None )
#     obj=models.Absence()
#     if form.is_valid():
#         obj.name_student=form.cleaned_data['name_student']
#         obj.date=form.cleaned_data['date']
#         obj.time=form.cleaned_data['time']
#         obj.Excuse=form.cleaned_data['Excuse']
#         obj.Reason=form.cleaned_data['Reason']
#         obj.save()
        
        
#     return render(request,'student/test.html',{'form':form})


def talemat(request):
    return render(request, 'darajat/talemat.html')    