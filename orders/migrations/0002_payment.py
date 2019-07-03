# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-03 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=100, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]