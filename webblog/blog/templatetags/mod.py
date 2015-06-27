# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.filter(name='mod')
def mod(value, arg):
    if not value:
        return value
    try:
        value = int(value)
        arg = int(arg)
    except TypeError:
        return value
    return value % arg
