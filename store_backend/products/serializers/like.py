from rest_framework import serializers

from products.models.products import Product


class GetLikeProduktSerializers(serializers.ModelSerializer):
    name = serializers.CharField(source='name.name')
    like = serializers.SerializerMethodField()
    dislike = serializers.SerializerMethodField()

    def get_like(self, obj):
        like = obj.feedback_product.filter(like=True).count()
        return like

    def get_dislike(self, obj):
        dislike = obj.feedback_product.filter(like=False).count()
        return dislike

    class Meta:
        model = Product
        fields = (
            'name',
            'like',
            'dislike'
        )


