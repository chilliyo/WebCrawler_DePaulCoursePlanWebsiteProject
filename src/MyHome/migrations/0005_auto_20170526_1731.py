# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 17:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyHome', '0004_auto_20170519_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='cs_Classes',
            fields=[
                ('class_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
                ('pre_req', models.CharField(max_length=1000)),
                ('class_type', models.CharField(max_length=100)),
                ('summer', models.BooleanField(default=False)),
                ('spring', models.BooleanField(default=False)),
                ('fall', models.BooleanField(default=False)),
                ('winter', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='is_Classes',
            fields=[
                ('class_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
                ('pre_req', models.CharField(max_length=1000)),
                ('class_type', models.CharField(max_length=100)),
                ('summer', models.BooleanField(default=False)),
                ('spring', models.BooleanField(default=False)),
                ('fall', models.BooleanField(default=False)),
                ('winter', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='asdf',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='concentration',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='full_name',
        ),
        migrations.AddField(
            model_name='signup',
            name='Classes_Per_Quarter',
            field=models.CharField(choices=[(b'1 Class', b'1 Class'), (b'2 Classes', b'2 Classes'), (b'3 Classes', b'3 Classes')], default=b'1', max_length=120),
        ),
        migrations.AddField(
            model_name='signup',
            name='First_Name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='Last_Name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='Major',
            field=models.CharField(choices=[(b'Computer Science (Standard Concentration)', b'Computer Science (Standard Concentration)'), (b'Information Systems (Business Analysis/Systems Analysis)', b'Information Systems (Business Analysis/Systems Analysis)'), (b'Information Systems (Business Intelligence Concentration)', b'Information Systems (Business Intelligence Concentration)'), (b'Information Systems (Database Administration Concentration)', b'Information Systems (Database Administration Concentration)'), (b'Information Systems (IT Enterprise Management Concentration)', b'Information Systems (IT Enterprise Management Concentration)'), (b'Information Systems (Standard Concentration)', b'Information Systems (Standard Concentration)')], default=b'Computer Science (Standard Concentration)', max_length=120),
        ),
        migrations.AddField(
            model_name='signup',
            name='Start_Quarter',
            field=models.CharField(choices=[(b'Fall', b'Fall'), (b'Winter', b'Winter'), (b'Spring', b'Spring')], default=b'Fall', max_length=120),
        ),
        migrations.AddField(
            model_name='signup',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='signup',
            name='summer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='classes_per_quarter',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)], verbose_name='classes_per_quarter'),
        ),
    ]
