from rest_framework.response import Response
from rest_framework.views import APIView

from products.models.shopping_car import Shopping_cart
from products.serializers.shopping_car import AllListShoppingCarSerializers
from products.services.shopping_car import AddShoppingCarService


class AddShoppingCarView(APIView):

    def post(self, request, **kwargs):
        data = AddShoppingCarService.execute({
            'user': request.user,
            'id': kwargs['id'],
            'amount': request.query_params['amount']
        })

        serializers = AllListShoppingCarSerializers(data, many=True).data
        return Response(serializers)
