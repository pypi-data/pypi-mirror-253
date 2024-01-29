from django.contrib import admin
from artd_customer.models import (
    Customer,
    Tag,
    CustomerTag,
    CustomerAddress,
    CustomerAdditionalFields,
)
from django_json_widget.widgets import JSONEditorWidget
from django.db import models


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
        "phone",
        "email",
        "partner__name",
    ]
    list_display = [
        "id",
        "name",
        "phone",
        "email",
        "status",
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = [
        "description",
    ]
    list_display = [
        "description",
    ]


@admin.register(CustomerTag)
class CustomerTagAdmin(admin.ModelAdmin):
    search_fields = [
        "customer",
        "tag",
    ]
    list_display = [
        "customer",
        "tag",
    ]


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    search_fields = [
        "customer__email",
        "city__name",
        "phone",
        "address",
    ]
    list_display = [
        "customer",
        "city",
        "phone",
        "address",
    ]
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }


@admin.register(CustomerAdditionalFields)
class CustomerAdditionalFieldsAdmin(admin.ModelAdmin):
    search_fields = [
        "partner__name",
        "name",
        "field_type",
        "label",
        "required",
    ]
    list_display = [
        "partner",
        "name",
        "field_type",
        "label",
        "required",
    ]
