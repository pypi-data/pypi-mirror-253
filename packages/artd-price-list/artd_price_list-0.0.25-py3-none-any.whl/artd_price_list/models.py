from django.db import models
from django.utils.translation import gettext_lazy as _
from artd_partner.models import Partner
from artd_product.models import Product
from django.utils import timezone


class PriceListBaseModel(models.Model):
    created_at = models.DateTimeField(
        _("Created at"),
        help_text=_("Created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        help_text=_("Updated at"),
        auto_now=True,
    )
    status = models.BooleanField(
        _("Status"),
        default=True,
        help_text=_("Status"),
    )
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        help_text=_("Partner"),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        help_text=_("Product"),
    )
    regular_price = models.DecimalField(
        "Price",
        max_digits=10,
        decimal_places=2,
        help_text=_("Price"),
    )
    special_price_from = models.DateTimeField(
        "Special price from",
        null=True,
        blank=True,
        help_text=_("Special price from"),
    )
    special_price_to = models.DateTimeField(
        "Special price to",
        null=True,
        blank=True,
        help_text=_("Special price to"),
    )
    special_price = models.DecimalField(
        "Special price",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_("Special price"),
    )

    class Meta:
        abstract = True


class PriceListLog(PriceListBaseModel):
    class Meta:
        verbose_name = _("Price list log")
        verbose_name_plural = _("Price list logs")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.product.name} ${self.regular_price} ({self.partner.name}))"


class PriceList(PriceListBaseModel):
    class Meta:
        unique_together = ("partner", "product")
        verbose_name = _("Price list")
        verbose_name_plural = _("Price lists")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.product.name} ${self.regular_price} ({self.partner.name}))"

    def get_real_price(self):
        if self.special_price:
            if self.special_price_from and self.special_price_to:
                if self.special_price_from <= timezone.now() <= self.special_price_to:
                    return self.special_price
                else:
                    return self.regular_price
            else:
                return self.special_price
        else:
            return self.regular_price

    def save(self, *args, **kwargs):
        PriceListLog.objects.create(
            partner=self.partner,
            product=self.product,
            regular_price=self.regular_price,
            special_price_from=self.special_price_from,
            special_price_to=self.special_price_to,
            special_price=self.special_price,
        )
        super(PriceList, self).save(*args, **kwargs)
