from django.contrib import admin
from student.models import Student, classstudent, masrofat, Category_masrof
# Register your models here.

admin.site.register(Student)
admin.site.register(classstudent)
admin.site.register(masrofat)
admin.site.register(Category_masrof)