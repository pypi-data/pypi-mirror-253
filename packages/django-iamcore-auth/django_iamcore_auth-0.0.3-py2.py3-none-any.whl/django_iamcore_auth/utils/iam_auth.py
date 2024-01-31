from django.utils.deprecation import MiddlewareMixin
from iamcore.client.exceptions import IAMUnauthorizedException
from iamcore.client.user import get_irn

from django_iamcore_auth.settings import IAM_ACCOUNT_NAME
from django_iamcore_auth.utils.headers import get_auth_headers


class IAMAuthenticationMiddleware(MiddlewareMixin):
    @staticmethod
    def authenticate(request):
        request.auth_headers = get_auth_headers(request.headers)
        request.irn = get_irn(request.auth_headers)
        if request.irn.account_id == 'anonymous':
            raise IAMUnauthorizedException("Not allowed anonymous access")
        if request.irn.account_id != IAM_ACCOUNT_NAME:
            raise IAMUnauthorizedException("Not allowed account")

    @staticmethod
    def authenticate_header(request):
        pass