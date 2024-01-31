import logging
from typing import Union, Dict

from django.http.request import HttpHeaders

logger = logging.getLogger(__name__)

BEARER_HEADER = 'authorization'
API_KEY_HEADER = 'x-iamcore-api-key'


def get_auth_headers(headers: HttpHeaders):
    if isinstance(headers, HttpHeaders):
        return {
            API_KEY_HEADER: headers.get('X-iamcore-API-Key'),
            BEARER_HEADER: headers.get('Authorization')
        }
    if isinstance(headers, dict):
        return {
            k.lower(): v
            for k, v in headers.items()
            if k.lower() in ('authorization', 'x-iamcore-api-key')
        }
    logger.error(f"Invalid headers class {headers.__class__} failed to extract auth headers.")
    return dict()
