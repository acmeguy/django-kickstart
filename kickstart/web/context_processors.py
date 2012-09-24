# coding=utf-8
from django.conf import settings

def web_settings(request):
    print settings.SKIN
    return {'SKIN': settings.SKIN }
