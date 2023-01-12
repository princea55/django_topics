from django import template
from django.core import signing
from django.core.signing import BadSignature

register = template.Library()
MENU_TYPES = {
    1: ['view-product', 'add_product', 'update_product', 'delete_product'],
}


def get_signed_value(value):
    return signing.dumps(value)


def get_unsigned_value(value, max_age=None):
    try:
        return signing.loads(value, max_age=max_age)
    except BadSignature:
        return None


@register.simple_tag()
def set_value(val):
    return val


@register.simple_tag()
def get_sign_pk(pk):
    return get_signed_value(pk)


@register.simple_tag()
def get_menu_selected_class(current_url, menu_type):
    if current_url in MENU_TYPES.get(menu_type):
        return 'show'
    return ''
