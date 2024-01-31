import logging
import sys
import traceback

from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponse
from iamcore.client.exceptions import IAMUnauthorizedException, IAMForbiddenException, IAMBedRequestException, \
    IAMConflictException

logger = logging.getLogger(__name__)


class IAMExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    @staticmethod
    def process_exception(request, exception):
        if isinstance(exception, IAMForbiddenException):
            return HttpResponseForbidden(exception.msg)
        if isinstance(exception, IAMUnauthorizedException):
            return HttpResponse(exception.msg, status=401)
        if isinstance(exception, IAMConflictException):
            return HttpResponse(exception.msg, status=409)
        if isinstance(exception, IAMBedRequestException):
            return HttpResponseBadRequest(exception.msg)
        exception_type, value, tb = sys.exc_info()
        logger.error("".join(traceback.format_exception(exception_type, value, tb)))
        return HttpResponseBadRequest(str(exception))
