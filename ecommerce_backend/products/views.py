from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from products.serializers import ProductSerializer
from products.models import Product, ProductImage


class ProductsAPI(APIView):
    def get(self, request: Request):
        products = Product.objects.all()
        products_serialized_list = list(map(lambda x: self.get_serialized_data(x.uid, request), products))
        return Response(products_serialized_list)

    def get_serialized_data(self, product_uid, request):
        product = Product.objects.get(uid=product_uid)
        data = ProductSerializer(product, context={"request": request}).data

        return data


class ProductDetailsAPI(APIView):
    def get(self, request: Request, uid: str):
        product = Product.objects.get(uid=uid)
        serializer = ProductSerializer(product)
        images = product.product_images.all()
        image_list = list(
            map(
                lambda x: request.build_absolute_uri(
                    reverse_lazy('product-image-download', kwargs={'image_uid': x.uid})),
                images
            )
        )
        data = serializer.data
        data['image_urls'] = image_list
        return Response(data)


class ProductImageDownloadAPI(APIView):
    def get(self, request: Request, image_uid):
        try:
            product_image = ProductImage.objects.get(uid=image_uid)
            if product_image.image:
                image_file = product_image.image.path
                with open(image_file, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='image/jpeg')
                    response['Content-Disposition'] = 'attachment; filename=' + product_image.image.name
                    return response
            else:
                return HttpResponseNotFound('Product image not found')
        except ProductImage.DoesNotExist:
            return HttpResponseNotFound('Product image not found')
