from django.contrib import admin
from student.models import Student, classstudent, masrofat, Category_masrof, mawad, Absence, hafela

# Register your models here.
admin.site.register(Student)
admin.site.register(Absence)
admin.site.register(classstudent)
admin.site.register(masrofat)
admin.site.register(Category_masrof)
admin.site.register(mawad)
admin.site.register(hafela)
