from rest_framework import serializers

from products.models.shopping_car import Shopping_cart


class AllListShoppingCarSerializers(serializers.ModelSerializer):
    client = serializers.CharField(source='client.username')
    product = serializers.CharField(source='product.name.name')

    class Meta:
        model = Shopping_cart
        fields = (
            'client',
            'product',
            'amount'
        )
