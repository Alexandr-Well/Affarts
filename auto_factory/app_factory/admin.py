from django.contrib import admin

from .models import Detail, CurrentAutoDetail, Auto, AutoPrice


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = (
        'detail_type', 'price'
    )


@admin.register(CurrentAutoDetail)
class CurrentAutoDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    pass


@admin.register(AutoPrice)
class AutoPriceAdmin(admin.ModelAdmin):
    pass
