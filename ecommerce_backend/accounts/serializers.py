from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.reverse import reverse_lazy

from order.models import Cart
from .models import User


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(write_only=True)
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'profile_image',
            'password',
            'download_url'
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        profile_image = validated_data.pop('profile_image', None)  # Remove profile_image from validated_data
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        cart = Cart()
        cart.user = instance
        cart.save()

        if profile_image is not None:
            instance.profile_image = profile_image
            instance.save()

        return instance

    def get_download_url(self, obj):
        if obj.profile_image:
            user_id = obj.id
            request: Request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(reverse_lazy('profile-image-download', kwargs={'user_id': user_id}))
        return None
