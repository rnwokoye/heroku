# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20171220_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotes',
            old_name='quotes_liked',
            new_name='quotes_participant',
        ),
    ]
