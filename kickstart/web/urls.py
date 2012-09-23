from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from .views import Home

urlpatterns = patterns('',
    # Signup, signin and signout
    (r'^$', Home.as_view(template_name="web/layouts/pricing_overview.html")),
)
