# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_delete_propertytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[(b'TerraceHouse', b'Terrace'), (b'BunglowHouse', b'Bunglow'), (b'Apartment', b'Apartment'), (b'DuplexHouse', b'Duplex')], max_length=255),
        ),
    ]
