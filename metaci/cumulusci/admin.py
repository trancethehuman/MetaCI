from django.contrib import admin

from metaci.cumulusci.models import Org, ScratchOrgInstance, Service


@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ("name", "repo", "scratch")
    list_filter = ("name", "scratch", "repo")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ScratchOrgInstance)
class ScratchOrgInstanceAdmin(admin.ModelAdmin):
    list_display = (
        "org",
        "build",
        "sf_org_id",
        "username",
        "org_note",
        "deleted",
        "time_created",
        "time_deleted",
    )
    list_filter = ("deleted", "org")
    raw_id_fields = ("build",)
