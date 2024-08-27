from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from products.serializers.users import ListUserSerializers, DataUserSerializers
from users.models import User


class PersonalProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializers = ListUserSerializers(request.user).data
        return Response(serializers, status=status.HTTP_200_OK)


class DataUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        serializers = DataUserSerializers(data=kwargs)
        serializers.is_valid(raise_exception=True)
        users_obj = serializers.validated_data['users_obj']
        ser_user = ListUserSerializers(users_obj).data
        return Response(ser_user, status=status.HTTP_200_OK)
