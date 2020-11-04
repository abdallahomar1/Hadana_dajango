# Generated by Django 3.1.2 on 2020-11-02 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classstudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('classtecher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Remaining_amount', models.IntegerField()),
                ('Time_add', models.DateTimeField(auto_now=True)),
                ('phone_father', models.IntegerField()),
                ('yourclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.classstudent')),
            ],
        ),
    ]
