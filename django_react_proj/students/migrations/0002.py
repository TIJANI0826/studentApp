# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2021-08-27 17:25
from __future__ import unicode_literals
from students.models import Student

from django.db import migrations, models

def create_data(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    Student(name="Joe Silver",email='joe@email.com',document="22342342",phone="000000000").save()
class Migration(migrations.Migration):

    # initial = True

    dependencies = [

        ('students','0001_initial')

    ]

    operations = [
        migrations.RunPython(create_data),
    ]

    # operations = [
    #     migrations.CreateModel(
    #         name='Student',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('name', models.CharField(max_length=240, verbose_name='Name')),
    #             ('email', models.EmailField(max_length=254)),
    #             ('document', models.CharField(max_length=20, verbose_name='Document')),
    #             ('phone', models.CharField(max_length=20)),
    #             ('registrationDate', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
    #         ],
    #     ),
    # ]