from django import template
from django.core import signing
from django.core.signing import BadSignature

register = template.Library()


def get_signed_value(value):
    return signing.dumps(value)


def get_unsigned_value(value, max_age=None):
    try:
        return signing.loads(value, max_age=max_age)
    except BadSignature:
        return None


@register.simple_tag()
def get_sign_pk(pk):
    return get_signed_value(pk)
