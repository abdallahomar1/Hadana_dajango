# Generated by Django 3.1.2 on 2020-11-03 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='img',
        ),
        migrations.AddField(
            model_name='student',
            name='imag',
            field=models.ImageField(default='noimg.png', upload_to='studentsimg/', verbose_name='الصورة'),
        ),
        migrations.AlterField(
            model_name='classstudent',
            name='classtecher',
            field=models.CharField(max_length=50, verbose_name='معلمة الفصل'),
        ),
        migrations.AlterField(
            model_name='classstudent',
            name='name',
            field=models.CharField(max_length=50, verbose_name='اسم الفصل'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Age',
            field=models.IntegerField(verbose_name='السن'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Remaining_amount',
            field=models.IntegerField(verbose_name='المبلغ المتبقي'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Time_add',
            field=models.DateTimeField(auto_now=True, verbose_name='وقت التقديم'),
        ),
        migrations.AlterField(
            model_name='student',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='المبلغ المدفوع'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_father',
            field=models.IntegerField(verbose_name='رقم هاتف الوالد'),
        ),
        migrations.AlterField(
            model_name='student',
            name='yourclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.classstudent', verbose_name='الفصل'),
        ),
    ]