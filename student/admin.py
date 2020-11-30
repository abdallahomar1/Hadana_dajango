from django.contrib import admin
from student.models import Student, classstudent, masrofat, Category_masrof, mawad, buses, Absence
# Register your models here.

admin.site.site_header = 'abdallah'
admin.site.site_title = 'admin panal'
class custom(admin.ModelAdmin):
    list_display = ('name','yourclass','amount_paid', 'Remaining_amount')
    list_filter = ('yourclass', 'Remaining_amount')
    search_fields = ('name','yourclass','amount_paid', 'Remaining_amount', 'Age', 'phone_father')
    list_per_page = 15
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('name_student','name_class', 'Excuse')

admin.site.register(Student, custom)
admin.site.register(Absence, AbsenceAdmin)
admin.site.register(classstudent)
admin.site.register(masrofat)
admin.site.register(Category_masrof)
admin.site.register(mawad)
admin.site.register(buses)
