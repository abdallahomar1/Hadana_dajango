from django.contrib import admin
from student.models import Student, classstudent, masrofat, Category_masrof, mawad, Absence, hafela, rateb
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.site_header = 'abdallah'
admin.site.site_title = 'admin panal'
class custom(admin.ModelAdmin):
    #list_display = ('name','yourclass','amount_paid', 'Remaining_amount')
    list_filter = ('yourclass', 'Remaining_amount')
    search_fields = ('name','yourclass','amount_paid', 'Remaining_amount', 'Age', 'phone_father')
    list_per_page = 15
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('name_student','name_class', 'Excuse')
class class_s(admin.ModelAdmin):
    list_display = ('name', 'classtecher')
@admin.register(Student)
class StudentImportEport(ImportExportModelAdmin):
    pass

admin.site.register(Absence, AbsenceAdmin)
admin.site.register(classstudent, class_s)

@admin.register(masrofat)
class masrofatImportEport(ImportExportModelAdmin):
    pass
@admin.register(Category_masrof)
class Category_masrofImportEport(ImportExportModelAdmin):
    pass
@admin.register(mawad)
class mawadImportEport(ImportExportModelAdmin):
    pass
@admin.register(hafela)
class hafelaImportEport(ImportExportModelAdmin):
    pass
@admin.register(rateb)
class ratebImportEport(ImportExportModelAdmin):
    pass

class ratebImportEport(ImportExportModelAdmin):
    list_display = ('name_techer')
