from urllib.parse import quote_plus
from django import template
from django.contrib.auth.models import User
from ..models import Tickets

register = template.Library()

@register.filter#(name='msgTicketstatus')
def msgTicketstatus(stt):
    if stt == 1:
        return " Available"
    else:
        return "Ticket sold out"

@register.filter
def infouser(thisid):
    fduser = None
    try:
        fduser = User.objects.get(id=thisid).first_name +" "+User.objects.get(id=thisid).last_name
    except Exception as ex:
        fduser = ex + ' Error Finding user'
    return fduser

