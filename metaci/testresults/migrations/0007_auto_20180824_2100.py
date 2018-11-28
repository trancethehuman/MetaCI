# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-24 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import metaci.testresults.models


class Migration(migrations.Migration):

    dependencies = [("testresults", "0006_testresultasset")]

    operations = [
        migrations.AlterField(
            model_name="testclass",
            name="test_type",
            field=models.CharField(
                choices=[
                    (b"Apex", b"Apex"),
                    (b"JUnit", b"JUnit"),
                    (b"Robot", b"Robot"),
                    (b"Other", b"Other"),
                ],
                db_index=True,
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="testresultasset",
            name="asset",
            field=models.FileField(upload_to=metaci.testresults.models.asset_upload_to),
        ),
    ]
