from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.filter()
def bold(value):
    if ":" in value:
        a, b, c = value.partition(":")
        return mark_safe('<strong>{}{}</strong>{}'.format(a, b, c))
    else:
        return value
