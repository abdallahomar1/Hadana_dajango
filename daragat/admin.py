from django.contrib import admin
from . models import daragat
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class custom(admin.ModelAdmin):
    #list_display = ('name_name')
    list_filter = ('clas', 'kind')
    search_fields = ('kind','name_name','clas')
    list_per_page = 15

# admin.site.register(daragat, custom)

@admin.register(daragat)
class daragatImportEport(ImportExportModelAdmin):
    pass
