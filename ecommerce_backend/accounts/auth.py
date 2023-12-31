import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request

from .models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request: Request):
        jwt_token = request.COOKIES.get('jwt')
        if jwt_token is None:
            return None

        try:
            payload = jwt.decode(jwt_token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

        user_id = payload['id']
        user = User.objects.filter(id=user_id).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        return user, None
