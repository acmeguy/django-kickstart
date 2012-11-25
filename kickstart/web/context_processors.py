# coding=utf-8
from django.conf import settings

def web_settings(request):
    return {'SKIN': settings.SKIN, 'NODEJS_FANOUT': settings.NODEJS_FANOUT }
