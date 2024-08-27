from django.contrib import admin

from .models import Country
from .models.city import City
from .models.feedbacks import Feedback
from .models.manufacturers import Manufacturer
from .models.products import Product
from .models.shopping_car import Shopping_cart
from .models.warehouse import Warehouse


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'measurement_unit')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('description',)


@admin.register(Shopping_cart)
class Shopping_cartAdmin(admin.ModelAdmin):
    list_display = ('product',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )
