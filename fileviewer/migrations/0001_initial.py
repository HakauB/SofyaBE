# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('data', models.FileField(max_length=255, upload_to='uploads/')),
                ('filetype', models.CharField(default='', max_length=255)),
            ],
            options={
                'ordering': ('submitted',),
            },
        ),
    ]