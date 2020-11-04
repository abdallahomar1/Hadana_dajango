from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name=("الاسم"))
    Age = models.IntegerField(verbose_name=("السن"))
    amount_paid = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=("المبلغ المدفوع"))
    imag = models.ImageField(upload_to='studentsimg/', default='noimg.png', verbose_name=("الصورة"))
    Remaining_amount = models.IntegerField(verbose_name=("المبلغ المتبقي"))
    Time_add = models.DateTimeField(auto_now=True, verbose_name=("وقت التقديم"))
    yourclass = models.ForeignKey('classstudent', on_delete=models.CASCADE, verbose_name=("الفصل"))
    phone_father = models.IntegerField(verbose_name=("رقم هاتف الوالد"))
    
    def __str__(self):
        return self.name

class classstudent(models.Model):
    name = models.CharField(max_length=50, verbose_name=("اسم الفصل"))
    classtecher = models.CharField(max_length=50, verbose_name=("معلمة الفصل"))

    def __str__(self):
        return self.name