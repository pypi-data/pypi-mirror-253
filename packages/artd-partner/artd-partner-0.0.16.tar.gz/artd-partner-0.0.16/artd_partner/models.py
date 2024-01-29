from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from artd_location.models import City


class PartnerBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField("status", default=True)

    class Meta:
        abstract = True


class Partner(PartnerBaseModel):
    """Model definition for Partner."""

    partner_slug = models.SlugField(
        _("slug"),
        help_text=_("Slug of headquarter"),
        max_length=150,
    )
    name = models.CharField(
        _("name"),
        help_text=_("Name of partner"),
        max_length=150,
    )
    dni = models.CharField(
        _("dni"),
        help_text=_("DNI of partner"),
        max_length=20,
    )
    email = models.EmailField(
        _("email"),
        help_text=_("Email of partner"),
        max_length=254,
    )
    city = models.ForeignKey(
        City,
        verbose_name=_("city"),
        help_text=_("City of partner"),
        on_delete=models.CASCADE,
    )
    address = models.CharField(
        _("address"),
        help_text=_("Address of partner"),
        max_length=250,
    )

    class Meta:
        """Meta definition for Partner."""

        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        """Unicode representation of Partner."""
        return self.name


class Headquarter(PartnerBaseModel):
    """Model definition for Headquarter."""

    name = models.CharField(
        _("name"),
        help_text=_("Name of headquarter"),
        max_length=150,
    )
    address = models.CharField(
        _("address"),
        help_text=_("Address of headquarter"),
        max_length=250,
    )
    city = models.ForeignKey(
        City,
        verbose_name=_("city"),
        help_text=_("City of headquarter"),
        on_delete=models.CASCADE,
    )
    phone = models.CharField(
        _("phone"),
        help_text=_("Phone of headquarter"),
        max_length=20,
    )
    partner = models.ForeignKey(
        Partner,
        verbose_name=_("partner"),
        help_text=_("Partner of headquarter"),
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for Headquarter."""

        verbose_name = "Headquarter"
        verbose_name_plural = "Headquarters"

    def __str__(self):
        """Unicode representation of Headquarter."""
        return self.name


class Position(PartnerBaseModel):
    """Model definition for Position."""

    name = models.CharField(
        _("name"),
        help_text=_("Name of position"),
        max_length=150,
    )

    class Meta:
        """Meta definition for Position."""

        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        """Unicode representation of Position."""
        return self.name


class Coworker(PartnerBaseModel):
    """Model definition for Coworker."""

    first_name = models.CharField(
        _("first_name"),
        help_text=_("First name of coworker"),
        max_length=150,
    )
    last_name = models.CharField(
        _("last_name"),
        help_text=_("Last name of coworker"),
        max_length=150,
    )
    dni = models.CharField(
        _("dni"),
        help_text=_("DNI of coworker"),
        max_length=20,
    )
    email = models.EmailField(
        _("email"),
        help_text=_("Email of coworker"),
        max_length=254,
    )
    phone = models.CharField(
        _("phone"),
        help_text=_("Phone of coworker"),
        max_length=20,
    )
    headquarter = models.ForeignKey(
        Headquarter,
        verbose_name=_("headquarter"),
        help_text=_("Headquarter of coworker"),
        on_delete=models.CASCADE,
    )
    position = models.ForeignKey(
        Position,
        verbose_name=_("position"),
        help_text=_("Position of coworker"),
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for Coworker."""

        verbose_name = "Coworker"
        verbose_name_plural = "Coworkers"

    def __str__(self):
        """Unicode representation of Coworker."""
        return self.first_name + " " + self.last_name
