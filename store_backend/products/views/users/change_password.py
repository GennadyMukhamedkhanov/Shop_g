from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from products.serializers.users import ListUserSerializers, DataUserSerializers, ChangePasswordSerializers
from users.models import User


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializers = ChangePasswordSerializers(
            data={
                'old_password': request.data.get('old_password'),
                'new_password': request.data.get('new_password'),
            },
            context={'user_obj': request.user}
        )
        serializers.is_valid(raise_exception=True)
        return Response(status=status.HTTP_201_CREATED)
