from django.conf import settings
from django.db.models import QuerySet
from django.db.utils import IntegrityError
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response

from order.models import Cart, CartItem
from order.serializers import CartSerializer
from rest_framework.views import APIView

from accounts.permissions import IsAuthenticated
from products.models import Product, SizeVariant, ColorVariant

import stripe


class CartDetailsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user = request.user
        cart = user.cart
        cart_serialized = CartSerializer(cart, context={'request': request})
        return Response(cart_serialized.data)


class AddItemToCartAPI(APIView):
    def post(self, request: Request):
        size_variant = None
        color_variant = None
        data = request.data
        user = request.user
        product = Product.objects.get(uid=data['product_uid'])
        try:
            size_variant = SizeVariant.objects.get(size_name=data['size_variant'])
        except KeyError:
            pass
        try:
            color_variant = ColorVariant.objects.get(color_name=data['color_variant'])
        except KeyError:
            pass

        cart_item = CartItem()
        cart_item.cart = user.cart
        cart_item.product = product
        cart_item.color_variant = color_variant
        cart_item.size_variant = size_variant
        try:
            cart_item.save()
        except IntegrityError:
            cart_item: CartItem = user.cart.cart_items.get(product=data['product_uid'])
            cart_item.item_count += 1
            cart_item.save()

        return Response("ok")


class RemoveItemFromCartAPI(APIView):
    def post(self, request: Request):
        cart_items: QuerySet = request.user.cart.cart_items
        try:
            cart_item = cart_items.get(uid=request.data['cart_uid'])
            if cart_item.item_count == 1:
                cart_item.delete()
            else:
                cart_item.item_count -= 1
                cart_item.save()
        except CartItem.DoesNotExist:
            pass

        return Response("Done")


class StripeCheckoutAPI(APIView):
    def post(self, request: Request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'unit_amount': 1000,
                    'product_data': {
                        'name': 'Your Product Name',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:3000/',  # URL to redirect to after successful payment
            cancel_url='http://127.0.0.1:3000/',
        )
        return JsonResponse({
            'session_id': session.stripe_id,
            'SPK': settings.STRIPE_PUBLISHABLE_KEY
        })
