from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import User
from rest_framework.exceptions import ValidationError


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username'], phone=attrs['phone'])
        if (not user.exists()) or (not user.first().check_password(attrs['password'])):
            raise ValidationError('Data is not valid')
        attrs['user'] = user.first()
        return attrs


class LogoutTokenSerializers(serializers.Serializer):

    def validate(self, attrs):
        token_obj = Token.objects.filter(user=self.context['user'])
        if not token_obj.exists():
            raise ValidationError('The user is not logged in')
        attrs['token_obj'] = token_obj.first()
        return attrs

