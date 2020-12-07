# Generated by Django 3.1.3 on 2020-11-30 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0005_remove_hafela_bus_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='daragat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('شهادة نصف العام', 'شهادة نصف العام'), ('شهادة نهاية العام', 'شهادة نهاية العام')], max_length=50, verbose_name='نوع الهادة')),
                ('kuran', models.IntegerField(default=40, verbose_name='درجة القران الكريم')),
                ('khades', models.IntegerField(default=30, verbose_name='درجة مادة الحديث')),
                ('arabek', models.IntegerField(default=30, verbose_name='درجة نور البيان')),
                ('serah', models.IntegerField(default=20, verbose_name='درجة مادة السيرة')),
                ('akeda', models.IntegerField(default=20, verbose_name='درجة مادة العقيدة')),
                ('athkar', models.IntegerField(default=20, verbose_name='درجة مادة الاذكار')),
                ('adab', models.IntegerField(default=20, verbose_name='درجة مادة الاداب')),
                ('en', models.IntegerField(default=20, verbose_name='درجة اللغة الانجليزية')),
                ('math', models.IntegerField(default=20, verbose_name='درجة مادة الرياضيات')),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.classstudent', verbose_name='اسم الفصل')),
                ('name_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='الاسم')),
            ],
            options={
                'verbose_name': 'الدرجات',
                'verbose_name_plural': 'الدرجات',
            },
        ),
    ]
