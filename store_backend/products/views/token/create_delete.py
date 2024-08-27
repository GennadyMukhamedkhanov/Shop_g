from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from products.serializers.token import TokenSerializer, LogoutTokenSerializers


class CreateTokenView(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.filter(user=user)
        if not token.exists():
            token = Token.objects.create(user=user)
        else:
            token = token.first()

        return Response(
            {'token': token.key},
            status=status.HTTP_201_CREATED
        )


class LogoutTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = LogoutTokenSerializers(data={}, context={'user': request.user})
        serializers.is_valid(raise_exception=True)
        token_obj = serializers.validated_data['token_obj']
        token_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
