"""
 * Copyright (C) ArtD SAS - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Written by Jonathan Favian Urzola Maldonado <jonathan@artd.com.co>, 2023
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from artd_location.models import City
from artd_partner.models import Partner

FIELD_TYPES = [
    ("number", _("Number")),
    ("date", _("Date")),
    ("email", _("Email")),
    ("password", _("Password")),
    ("text", _("Text")),
]


class CustomerBaseModel(models.Model):
    created_at = models.DateTimeField(
        _("Created at"),
        help_text=_("Date time on which the object was created."),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        help_text=_("Date time on which the object was last updated."),
        auto_now=True,
        editable=False,
    )
    status = models.BooleanField(
        _("Status"),
        help_text=_("Status of the object."),
        default=True,
    )

    class Meta:
        abstract = True


class Customer(CustomerBaseModel):
    name = models.CharField(
        _("Name"),
        help_text=_("Name of the customer."),
        max_length=100,
        blank=True,
    )
    last_name = models.CharField(
        _("Last name"),
        help_text=_("Last name of the customer."),
        max_length=100,
        blank=True,
        null=True,
    )
    birth_date = models.DateField(
        _("Birth date"),
        help_text=_("Birth date of the customer."),
        blank=True,
        null=True,
    )
    document = models.CharField(
        _("Customer document"),
        max_length=50,
        help_text=_("Customer document"),
        blank=True,
        null=True,
    )
    email = models.EmailField(
        _("Email"),
        help_text=_("Email of the customer."),
        max_length=100,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        _("Phone"),
        help_text=_("Phone of the customer."),
        max_length=100,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City,
        verbose_name=_("City"),
        help_text=_("City of the customer."),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    other_data = models.JSONField(
        _("Other data"),
        help_text=_("Other customer data"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name


class Tag(CustomerBaseModel):
    partner = models.ForeignKey(
        Partner,
        verbose_name=_("Partner"),
        help_text=_("Partner of the tag."),
        on_delete=models.CASCADE,
    )

    description = models.CharField(
        _("Tag description"),
        max_length=250,
        help_text=_("Tag description"),
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.description


class CustomerTag(CustomerBaseModel):
    customer = models.ForeignKey(
        Customer,
        verbose_name=_("Customer"),
        help_text=_("Customer"),
        on_delete=models.CASCADE,
    )
    tag = models.ForeignKey(
        Tag,
        verbose_name=_("Customer tag"),
        help_text=_("Tag."),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Customer Tag"
        verbose_name_plural = "Customer Tags"

    def __str__(self):
        return self.customer.name + " - " + self.tag.description


class CustomerAddress(CustomerBaseModel):
    customer = models.ForeignKey(
        Customer,
        verbose_name=_("Customer"),
        help_text=_("Customer"),
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        City,
        verbose_name=_("City"),
        help_text=_("City of the customer."),
        on_delete=models.CASCADE,
    )
    phone = models.CharField(
        _("Phone"),
        max_length=50,
        help_text=_("Customer phone"),
        blank=True,
        null=True,
    )
    address = models.TextField(
        _("Customer address"),
        help_text=_("Customer address"),
        blank=True,
        null=True,
    )
    other_data = models.JSONField(
        _("Other data"),
        help_text=_("Other customer address data"),
        blank=True,
        null=True,
    )

    class Meta:
        """Meta definition for CustomerAddress."""

        verbose_name = _("Customer Address")
        verbose_name_plural = _("Customer Addresss")

    def __str__(self):
        """Unicode representation of CustomerAddress."""
        return f"{self.customer} {self.address}"


class CustomerAdditionalFields(CustomerBaseModel):
    partner = models.ForeignKey(
        Partner,
        verbose_name=_("Partner"),
        help_text=_("Partner of the field."),
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        "Field name",
        help_text="Field name",
        max_length=250,
    )
    field_type = models.CharField(
        _("Field type"),
        help_text=_("Field type"),
        max_length=10,
        choices=FIELD_TYPES,
    )
    label = models.CharField(
        _("Field label"),
        max_length=50,
        help_text=_("Field label"),
    )
    required = models.BooleanField(
        _("Is required?"),
        help_text=_("Is required?"),
        default=False,
    )

    class Meta:
        """Meta definition for CustomerAdditionalFields."""

        verbose_name = _("Customer Additional Field")
        verbose_name_plural = _("Customer Additional Fields")

    def __str__(self):
        """Unicode representation of CustomerAdditionalFields."""
        return f"{self.name}"
