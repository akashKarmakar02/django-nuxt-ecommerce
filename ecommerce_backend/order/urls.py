from django.urls import path
from order.views import CartDetailsAPI, AddItemToCartAPI, RemoveItemFromCartAPI, StripeCheckoutAPI


urlpatterns = [
    path('', CartDetailsAPI.as_view()),
    path('add/', AddItemToCartAPI.as_view()),
    path('remove/', RemoveItemFromCartAPI.as_view()),
    path('checkout/', StripeCheckoutAPI.as_view()),
]
