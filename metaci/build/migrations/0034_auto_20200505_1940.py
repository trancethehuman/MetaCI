# Generated by Django 2.2.11 on 2020-05-05 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0033_build_org_api_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='builds', to='repository.Branch'),
        ),
        migrations.AlterField(
            model_name='build',
            name='current_rebuild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_builds', to='build.Rebuild'),
        ),
        migrations.AlterField(
            model_name='build',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='builds', to='cumulusci.Org'),
        ),
        migrations.AlterField(
            model_name='build',
            name='org_instance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='builds', to='cumulusci.ScratchOrgInstance'),
        ),
        migrations.AlterField(
            model_name='build',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='builds', to='plan.Plan'),
        ),
        migrations.AlterField(
            model_name='build',
            name='planrepo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='builds', to='plan.PlanRepository'),
        ),
        migrations.AlterField(
            model_name='build',
            name='release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='release.Release'),
        ),
        migrations.AlterField(
            model_name='rebuild',
            name='org_instance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rebuilds', to='cumulusci.ScratchOrgInstance'),
        ),
        migrations.AlterField(
            model_name='rebuild',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rebuilds', to=settings.AUTH_USER_MODEL),
        ),
    ]
