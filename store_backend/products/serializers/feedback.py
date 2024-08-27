from rest_framework import serializers

from products.models.feedbacks import Feedback
from users.models import User


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class ListFeedbackSerializers(serializers.ModelSerializer):
    client = UsersSerializers()
    product = serializers.CharField(source='product.name')

    class Meta:
        model = Feedback
        fields = (
            'description',
            'like',
            'client',
            'product'
        )
