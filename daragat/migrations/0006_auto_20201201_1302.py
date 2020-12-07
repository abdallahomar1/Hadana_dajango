# Generated by Django 3.1.3 on 2020-12-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daragat', '0005_auto_20201130_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daragat',
            name='kind',
            field=models.CharField(choices=[('شهادة نصف العام', 'شهادة نصف العام'), ('شهادة نهاية العام', 'شهادة نهاية العام')], max_length=50, null=True, verbose_name='نوع الشهادة'),
        ),
    ]