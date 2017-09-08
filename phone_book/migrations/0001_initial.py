# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-01 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('is_mobile', models.BooleanField(default=True, verbose_name='Mobile')),
            ],
        ),
        migrations.CreateModel(
            name='Sign_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='phone_number',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone_book.Sign_Name'),
        ),
    ]
