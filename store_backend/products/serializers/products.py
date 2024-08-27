from rest_framework import serializers

from products.models.manufacturers import Manufacturer
from products.models.products import Product
from products.models.warehouse import Warehouse

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = (
            'name',
            'description'
        )
class ListWarehouseSerializers(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()


    class Meta:
        model = Warehouse
        fields = (
            'name',
            'amount',
            'manufacturer'
        )


class ListProductsSerializers(serializers.ModelSerializer):
    name = ListWarehouseSerializers()


    def get_name(self, obj):
        ser_warehouse = ListWarehouseSerializers(obj).data
        return ser_warehouse

    class Meta:
        model = Product
        fields = (
            "name",
            "cost_product",
            "measurement_unit",
            "description",
            "image",
        )
