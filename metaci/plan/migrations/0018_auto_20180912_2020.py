# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-12 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("repository", "0005_repository_release_tag_regex"),
        ("plan", "0017_merge_20180911_1915"),
    ]

    operations = [
        migrations.RemoveField(model_name="plan", name="test_dashboard"),
        migrations.AlterUniqueTogether(
            name="planrepository", unique_together=set([("plan", "repo")])
        ),
    ]
