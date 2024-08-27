from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Country
from products.serializers.country import CountrySerializers


class ListCountry(APIView):
    def get(self, request):
        country_all = Country.objects.all()
        ser = CountrySerializers(country_all, many=True).data
        return Response(ser)