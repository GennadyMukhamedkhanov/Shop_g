from rest_framework import serializers

from products.models import Country
from products.models.city import City


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)

class CountrySerializers(serializers.ModelSerializer):
    city =CitySerializers(many=True)




    class Meta:
        model = Country
        fields = (
            'name',
            'city'
        )