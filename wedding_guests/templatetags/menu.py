from django import template

from ..models import Page


register = template.Library()

@register.simple_tag
def menu_pages():
    return Page.objects.order_by('order_no')
