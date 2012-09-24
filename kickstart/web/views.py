# some_app/views.py
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "web/pages/about_us.html"

    def get_context_data(self, **kwargs):
        print kwargs
        return super(Home, self).get_context_data(**kwargs)



