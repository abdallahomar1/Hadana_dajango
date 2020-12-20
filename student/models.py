from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name=("الاسم"), null=True)
    numer = models.CharField(verbose_name=("الرقم القومي"), default=0, max_length=50)
    Age = models.IntegerField(verbose_name=("السن"))
    amount_paid = models.IntegerField(verbose_name=("المبلغ المدفوع"))
    imag = models.ImageField(upload_to='studentsimg/', default='noimg.png', verbose_name=("الصورة"))
    Remaining_amount = models.IntegerField(verbose_name=("المبلغ المتبقي"))
    Time_add = models.DateTimeField(auto_now=True, verbose_name=("وقت التقديم"))
    yourclass = models.ForeignKey('classstudent', on_delete=models.CASCADE, verbose_name=("الفصل"))
    phone_father = models.CharField(verbose_name=("رقم هاتف الوالد"),max_length=50)
    bus = models.ForeignKey("hafela", on_delete=models.CASCADE, verbose_name=("الحافلة"), null=True, blank=True)
    

    class Meta:
        verbose_name = _("الطلاب")
        verbose_name_plural = _("الطلاب")

    
    def __str__(self):
        return self.name

class classstudent(models.Model):
    name = models.CharField(max_length=50, verbose_name=("اسم الفصل"))
    classtecher = models.CharField(max_length=50, verbose_name=("معلمة الفصل"))
    mada = models.ManyToManyField("mawad", verbose_name=("المواد"))

    class Meta:
        verbose_name = _("الفصول")
        verbose_name_plural = _("الفصول")
    def __str__(self):
        return self.name

class masrofat(models.Model):
    Category = models.ForeignKey('Category_masrof', on_delete=models.CASCADE, verbose_name=("التصنيف"))
    des_masrofat =  models.CharField(max_length=95, verbose_name=("وصف المستلزم"))
    price_masrofat = models.IntegerField(verbose_name=("سعر المستلزم"))

    class Meta:
        verbose_name = _("المصروفات")
        verbose_name_plural = _("المصروفات")

    def __str__(self):
        return self.des_masrofat

class Category_masrof(models.Model):
    name = models.CharField(max_length=50, verbose_name=("اسم التصنيف"))

    class Meta:
        verbose_name = _("تصنيفات المصروفات")
        verbose_name_plural = _("تصنيفات المصروفات")

    def __str__(self):
        return self.name

class mawad(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("المواد")
        verbose_name_plural = _("المواد")

    def __str__(self):
        return self.name


class Absence(models.Model):
    name_class = models.ForeignKey(classstudent, on_delete=models.CASCADE, verbose_name=("اسم الفصل")) 
    name_student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=("اسم الطالب")) #(Student, verbose_name=("اسم الطالب"))
    time = models.DateField()  
    Excuse = models.BooleanField(default=True, verbose_name=("بعذر ام لا"))   
    Reason = models.TextField(verbose_name=("العذر"), null=True)

    class Meta:
        verbose_name = _("الغياب")
        verbose_name_plural = _("الغياب")

class hafela(models.Model):
    nam = models.CharField(max_length=50, verbose_name=("اسم السائق"))
    bus_id = models.CharField(max_length=50, verbose_name=("رقم الحافلة"))
    bus_price = models.IntegerField(verbose_name=("السعر الشهري"))
    #bus_student = models.ManyToManyField(Student, verbose_name=("اطفال الحافلة"), null=True)

    def __str__(self):
        return self.nam

    class Meta:
        verbose_name = _("الحافلات")
        verbose_name_plural = _("الحافلات")    
class rateb(models.Model):
    name_techer = models.OneToOneField(classstudent, on_delete=models.CASCADE, verbose_name=("اسم المعلمة"))
    yuor_rateb = models.IntegerField(verbose_name=("الراتب"))

    def __str__(self):
        return self.name_techer
    class Meta:
        verbose_name = _("الرواتب")
        verbose_name_plural = _("الرواتب")