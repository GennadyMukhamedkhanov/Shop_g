from rest_framework.response import Response
from rest_framework.views import APIView
from products.serializers.shopping_car import AllListShoppingCarSerializers
from products.services.shopping_car import AddShoppingCarService, DelShoppingCarService


class DelShoppingCarView(APIView):

    def post(self, request, **kwargs):
        data = DelShoppingCarService.execute({
            'user': request.user,
            'id': kwargs['id'],
            'amount': request.query_params['amount']
        })

        serializers = AllListShoppingCarSerializers(data, many=True).data
        return Response(serializers)
