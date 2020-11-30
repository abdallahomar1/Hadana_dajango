# Generated by Django 3.1.3 on 2020-11-30 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم السائق')),
                ('filld', models.CharField(default='aaa', max_length=50, null=True, verbose_name='رقم الاتوبس')),
                ('salary', models.IntegerField(verbose_name='السعر الشهري')),
            ],
        ),
        migrations.CreateModel(
            name='Category_masrof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم التصنيف')),
            ],
            options={
                'verbose_name': 'تصنيفات المصروفات',
                'verbose_name_plural': 'تصنيفات المصروفات',
            },
        ),
        migrations.CreateModel(
            name='classstudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم الفصل')),
                ('classtecher', models.CharField(max_length=50, verbose_name='معلمة الفصل')),
            ],
            options={
                'verbose_name': 'الفصول',
                'verbose_name_plural': 'الفصول',
            },
        ),
        migrations.CreateModel(
            name='mawad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'المواد',
                'verbose_name_plural': 'المواد',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الاسم')),
                ('Age', models.IntegerField(verbose_name='السن')),
                ('amount_paid', models.IntegerField(verbose_name='المبلغ المدفوع')),
                ('imag', models.ImageField(default='noimg.png', upload_to='studentsimg/', verbose_name='الصورة')),
                ('Remaining_amount', models.IntegerField(verbose_name='المبلغ المتبقي')),
                ('Time_add', models.DateTimeField(auto_now=True, verbose_name='وقت التقديم')),
                ('phone_father', models.IntegerField(verbose_name='رقم هاتف الوالد')),
                ('yourclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.classstudent', verbose_name='الفصل')),
            ],
            options={
                'verbose_name': 'الطلاب',
                'verbose_name_plural': 'الطلاب',
            },
        ),
        migrations.CreateModel(
            name='masrofat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_masrofat', models.CharField(max_length=95, verbose_name='وصف المستلزم')),
                ('price_masrofat', models.IntegerField(verbose_name='سعر المستلزم')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.category_masrof', verbose_name='التصنيف')),
            ],
            options={
                'verbose_name': 'المصروفات',
                'verbose_name_plural': 'المصروفات',
            },
        ),
        migrations.AddField(
            model_name='classstudent',
            name='mada',
            field=models.ManyToManyField(to='student.mawad', verbose_name='المواد'),
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('Excuse', models.BooleanField(default=True, verbose_name='بعذر ام لا')),
                ('Reason', models.TextField(null=True, verbose_name='العذر')),
                ('name_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.classstudent', verbose_name='اسم الفصل')),
                ('name_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='اسم الطالب')),
            ],
            options={
                'verbose_name': 'الغياب',
                'verbose_name_plural': 'الغياب',
            },
        ),
    ]
