from rest_framework.response import Response
from rest_framework.views import APIView

from products.serializers.shopping_car import AllListShoppingCarSerializers
from products.services.shopping_car import AllListShoppingCarService


class ListShoppingCarView(APIView):

    def get(self, request):
        data = AllListShoppingCarService.execute({'user': request.user})

        serializers = AllListShoppingCarSerializers(data, many=True).data
        return Response(serializers)
