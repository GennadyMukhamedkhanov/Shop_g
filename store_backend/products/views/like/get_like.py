from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.serializers.like import GetLikeProduktSerializers
from products.services.like import GetLikeProduktServices, AddLikeServices, AddDislikeServices


class GetProductLikeView(APIView):
    def get(self, request, **kwargs):
        product_obj = GetLikeProduktServices.execute(kwargs)
        serializers = GetLikeProduktSerializers(product_obj).data
        return Response(serializers)


class ProductAddLikeView(APIView):
    def post(self, request, **kwargs):
        AddLikeServices.execute({
            'id': kwargs['id'],
            'user': request.user,
            'description': request.query_params.get('description', '')

        })

        return Response(status=status.HTTP_201_CREATED)


class ProductAddDislikeView(APIView):
    def post(self, request, **kwargs):
        AddDislikeServices.execute({
            'id': kwargs['id'],
            'user': request.user,
            'description': request.query_params.get('description', '')
        })

        return Response(status=status.HTTP_201_CREATED)
