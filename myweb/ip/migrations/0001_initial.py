# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-10-11 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iptable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'indexes': [],
            },
        ),
    ]
