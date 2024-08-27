from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from products.serializers.users import ListUserSerializers, CreareUserSerializzer
from users.models import User


class UserListCreateView(APIView):
    def get(self, request):
        page_size = request.query_params.get('page_size')
        users = User.objects.all()
        pagination = PageNumberPagination()
        if page_size and int(page_size) > 0:
            pagination.page_size = page_size
        paginate_queryset = pagination.paginate_queryset(users, request)
        serializers = ListUserSerializers(paginate_queryset, many=True).data
        return pagination.get_paginated_response(serializers)

    def post(self, request):
        serializers = CreareUserSerializzer(data=request.data)
        serializers.is_valid(raise_exception=True)
        users = serializers.validated_data['user']
        return Response(ListUserSerializers(users).data, status=status.HTTP_201_CREATED)
