from django import template
from teamspirit.models import Session

register = template.Library()

@register.filter(name='get_stats')
def get_stats(value, arg):
    if len(value.filter(session=Session.objects.get(id=arg))) == 0:
        return None
    else:
        return value.filter(session=Session.objects.get(id=arg))