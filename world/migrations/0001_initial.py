# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.29 on 2020-04-09 09:54
=======
# Generated by Django 1.11.29 on 2020-04-08 13:21
>>>>>>> b0e884ed60785b5910bda8bdecfbccd4688d3d85
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(default='', max_length=254)),
<<<<<<< HEAD
                ('image', models.ImageField(upload_to='images')),
=======
                ('image', models.ImageField(upload_to='images_places')),
>>>>>>> b0e884ed60785b5910bda8bdecfbccd4688d3d85
            ],
        ),
    ]
