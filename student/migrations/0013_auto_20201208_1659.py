# Generated by Django 3.1.3 on 2020-12-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20201203_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='time',
            field=models.DateField(),
        ),
    ]