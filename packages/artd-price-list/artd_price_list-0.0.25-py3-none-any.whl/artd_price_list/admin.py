from django.contrib import admin
from .models import PriceList, PriceListLog


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "partner",
        "product",
        "regular_price",
        "special_price_from",
        "special_price_to",
        "special_price",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "partner",
        "product",
    )
    search_fields = (
        "id",
        "partner__name",
        "product__name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(PriceListLog)
class PriceListLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "partner",
        "product",
        "regular_price",
        "special_price_from",
        "special_price_to",
        "special_price",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "partner",
        "product",
    )
    search_fields = (
        "id",
        "partner__name",
        "product__name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
