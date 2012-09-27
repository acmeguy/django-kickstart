# some_app/views.py
from django.views.generic import TemplateView, FormView
from kickstart.web.forms import ContactUsForm

class Home(TemplateView):
    template_name = "web/pages/about_us.html"

    def get_context_data(self, **kwargs):
        print kwargs
        return super(Home, self).get_context_data(**kwargs)

class ContactUs(FormView):
    form_class      = ContactUsForm
    template_name   = "web/pages/contact_us.html"
    success_url = '/'
    #success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactUs, self).form_valid(form)

