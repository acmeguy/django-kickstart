from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from .views import Home

urlpatterns = patterns('',
    # Signup, signin and signout
    (r'^$', Home.as_view(template_name="web/layouts/services_overview.html")),
)
