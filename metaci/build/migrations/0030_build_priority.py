# Generated by Django 2.2.5 on 2019-10-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("build", "0029_build_org_note")]

    operations = [
        migrations.AddField(
            model_name="build", name="priority", field=models.IntegerField(default=0)
        )
    ]
