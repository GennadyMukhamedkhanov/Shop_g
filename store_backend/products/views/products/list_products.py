from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from conf.settings import TIME_CACHE
from products.models.products import Product
from products.serializers.products import ListProductsSerializers
from utils.cache import cache


class ListProductsView(APIView):
    @cache(time_cache=TIME_CACHE)
    def get(self, request):
        # Todo send_spam_email.delay('dumgreshmen@mail.ru')
        # Todo send_spam_every_5_second.delay()

        page_size = request.query_params.get('page_size')
        pagination = PageNumberPagination()
        products_queryset = Product.objects.all()
        if page_size and int(page_size) > 0:
            pagination.page_size = page_size
        paginate_queryset = pagination.paginate_queryset(products_queryset, request)
        serializers = ListProductsSerializers(paginate_queryset, many=True).data
        return pagination.get_paginated_response(serializers)




class ProductsView(APIView):

    def get(self, *args, **kwargs):
        product = Product.objects.get(id=kwargs['id'])
        serializers = ListProductsSerializers(product).data
        return Response(serializers, status=status.HTTP_200_OK)
