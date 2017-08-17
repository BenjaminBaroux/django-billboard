# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='empty title', max_length=100, null=True)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]