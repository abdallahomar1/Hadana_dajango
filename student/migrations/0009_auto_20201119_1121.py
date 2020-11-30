# Generated by Django 3.1.3 on 2020-11-19 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20201118_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='Reason',
            field=models.TextField(verbose_name='العذر'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='name_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.classstudent', verbose_name='اسم الفصل'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='name_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='اسم الطالب'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
