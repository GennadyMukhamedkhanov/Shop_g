from rest_framework import serializers

from users.models import User


class ListUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
        )


class CreareUserSerializzer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.create_user(**attrs)
        attrs['user'] = user
        return attrs


class DataUserSerializers(serializers.Serializer):
    id = serializers.IntegerField()

    def validate(self, attrs):
        users_obj = User.objects.filter(id=attrs['id'])
        if not users_obj.exists():
            raise Exception('The user was not found')
        attrs['users_obj'] = users_obj.first()
        return attrs


class ChangePasswordSerializers(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, attrs):
        user_obj = self.context.get('user_obj')
        if not user_obj.check_password(attrs['old_password']):
            raise Exception('The password is incorrect')
        user_obj.set_password(attrs['new_password'])
        user_obj.save()
        return True

