# Generated by Django 3.1.3 on 2020-11-30 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_hafela_bus_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hafela',
            name='bus_student',
        ),
    ]
