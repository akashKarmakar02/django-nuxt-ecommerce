from django.urls import path

from products.views import ProductsAPI, ProductImageDownloadAPI, ProductDetailsAPI


urlpatterns = [
    path('', ProductsAPI.as_view()),
    path('<slug:uid>', ProductDetailsAPI.as_view()),
    path('product_image_download/<slug:image_uid>', ProductImageDownloadAPI.as_view(), name='product-image-download')
]
