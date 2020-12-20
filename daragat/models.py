from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
shahada_type = (
    ('شهادة نصف العام','شهادة نصف العام'),
    ('شهادة نهاية العام','شهادة نهاية العام'),
) 

class daragat(models.Model):
    kind = models.CharField(max_length=50, choices=shahada_type, verbose_name=("نوع الشهادة"), null=True)
    name_name = models.ForeignKey("student.Student", on_delete=models.CASCADE, verbose_name=("الاسم"))
    clas = models.ForeignKey("student.classstudent", on_delete=models.CASCADE, verbose_name=("اسم الفصل"))
    kuran = models.IntegerField(default=40, verbose_name=("درجة القران الكريم"))
    khades = models.IntegerField(default=30, verbose_name=("درجة مادة الحديث"))
    arabek = models.IntegerField(default=30, verbose_name=("درجة نور البيان"))
    serah = models.IntegerField(default=20, verbose_name=("درجة مادة السيرة"))
    akeda = models.IntegerField(default=20, verbose_name=("درجة مادة العقيدة"))
    athkar = models.IntegerField(default=20, verbose_name=("درجة مادة الاذكار")) 
    adab = models.IntegerField(default=20, verbose_name=("درجة مادة الاداب"))
    en = models.IntegerField(default=20, verbose_name=("درجة اللغة الانجليزية"))
    math = models.IntegerField(default=20, verbose_name=("درجة مادة الرياضيات"))

    def __str__(self):
        return self.name_name

    def majmoa(self):
        majemoa = self.kuran + self.khades + self.arabek + self.serah + self.akeda + self.athkar + self.adab + self.en + self.math
        return majemoa

    class Meta:
        verbose_name = _("الدرجات")
        verbose_name_plural = _("الدرجات")

    
    