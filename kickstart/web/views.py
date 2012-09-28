# some_app/views.py
from django.views.generic import TemplateView, FormView
from kickstart.web.forms import ContactUsForm, FanOutForm
import redis
import json

class Home(TemplateView):
    template_name = "web/pages/about_us.html"

    def get_template_names(self):

        return super(Home, self).get_template_names()


    def get_context_data(self, **kwargs):

        return super(Home, self).get_context_data(**kwargs)


class FanOut(FormView):
    template_name = "web/pages/fan_out.html"
    form_class      = FanOutForm
    success_url = '/send_message/'

    def form_valid(self, form):
        redis_subscribe = redis.StrictRedis()
        message = form.cleaned_data['message']
        redis_subscribe.publish('socketio_news',json.dumps({'title':message}))
        return super(FanOut, self).form_valid(form)

class ContactUs(FormView):
    form_class      = ContactUsForm
    template_name   = "web/pages/contact_us.html"
    success_url = '/'
    #success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactUs, self).form_valid(form)

