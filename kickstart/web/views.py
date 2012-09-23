# some_app/views.py
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "web/about.html"