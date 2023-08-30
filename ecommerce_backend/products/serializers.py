from rest_framework import serializers
from rest_framework.reverse import reverse_lazy
from rest_framework.serializers import StringRelatedField, CharField
from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    category = CharField(source='category.category_name')
    color_variant = StringRelatedField(many=True)
    size_variant = StringRelatedField(many=True)
    image_urls = serializers.SerializerMethodField()

    def get_image_urls(self, product):
        request = self.context.get('request')
        if request is not None and product.product_images.exists():
            product_image = product.product_images.first()
            image_url = request.build_absolute_uri(reverse_lazy('product-image-download', kwargs={'image_uid': str(product_image.uid)}))
            return image_url
        return None

    class Meta:
        model = Product
        fields = [
            'uid',
            'product_name',
            'slug',
            'category',
            'price',
            'product_description',
            'color_variant',
            'size_variant',
            'image_urls'
        ]
