from django.shortcuts import render
from  . models import Student, classstudent, masrofat, Category_masrof
from django.db.models import Sum


#from . all_rebh_hadana import arbah
# Create your views here.

def all_student(request):
    student_list = Student.objects.all()
    context = {
        'students':student_list
    }
    return render(request, 'student/all_students.html', context)


def student_one(request, id):
    student_one = Student.objects.get(id=id)
    student_img = Student.objects.all()
    
    context = {'onestudent':student_one, 'imagestudent':student_img}
    return render(request, 'student/student.html', context)

def rebh(request):
    pass