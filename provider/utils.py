from __future__ import absolute_import

import hashlib
import shortuuid
from datetime import datetime, tzinfo
from django.conf import settings
from .constants import EXPIRE_DELTA, EXPIRE_CODE_DELTA

try:
    from django.utils import timezone
except ImportError:
    timezone = None


def now():
    if timezone:
        return timezone.now()
    else:
        # Django 1.3 compatibility
        return datetime.now()


def short_token():
    """
    Generate a hash that can be used as an application identifier
    """
    hash = hashlib.sha1(shortuuid.uuid().encode("utf-8"))
    hash.update(settings.SECRET_KEY.encode("utf-8"))
    return hash.hexdigest()[::2]


def long_token():
    """
    Generate a hash that can be used as an application secret
    """
    hash = hashlib.sha1(shortuuid.uuid().encode("utf-8"))
    hash.update(settings.SECRET_KEY.encode("utf-8"))
    return hash.hexdigest()


def get_token_expiry():
    """
    Return a datetime object indicating when an access token should expire.
    Can be customized by setting :attr:`settings.OAUTH_EXPIRE_DELTA` to a
    :attr:`datetime.timedelta` object.
    """
    return now() + EXPIRE_DELTA


def get_code_expiry():
    """
    Return a datetime object indicating when an authorization code should
    expire.
    Can be customized by setting :attr:`settings.OAUTH_EXPIRE_CODE_DELTA` to a
    :attr:`datetime.timedelta` object.
    """
    return now() + EXPIRE_CODE_DELTA
