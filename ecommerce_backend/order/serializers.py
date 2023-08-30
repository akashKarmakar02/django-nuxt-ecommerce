from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from order.models import Cart, CartItem
from products.serializers import ProductSerializer


class CartItemsSerializer(ModelSerializer):
    product = ProductSerializer()
    size_variant = StringRelatedField()
    color_variant = StringRelatedField()

    class Meta:
        model = CartItem
        fields = [
            'uid',
            'product',
            'item_count',
            'color_variant',
            'size_variant',
        ]


class CartSerializer(ModelSerializer):
    cart_items = CartItemsSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            'user',
            'cart_items'
        ]
