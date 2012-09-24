from django.conf.urls import patterns, url
from views import Home

urlpatterns = patterns('',
    # Signup, signin and signout
    url(r'^$', Home.as_view(template_name="web/pages/about_us.html"),name="home"),
    url(r'^about_us/', Home.as_view(template_name="web/pages/about_us.html"),name="about"),
    url(r'^blog/(?P<slug>\w+)/$', Home.as_view(template_name="web/pages/blog_post.html"),name="blogpost"),
    url(r'^blog/', Home.as_view(template_name="web/pages/blog_overview.html"),name="blog"),
    url(r'^faq/', Home.as_view(template_name="web/pages/faq_list.html"),name="faq"),
    url(r'^pricing/', Home.as_view(template_name="web/pages/pricing_overview.html"),name="pricing"),
    url(r'^services/', Home.as_view(template_name="web/pages/services_overview.html"),name="services"),
    url(r'^testimonials/', Home.as_view(template_name="web/pages/testimonials.html"),name="testimonials"),
    url(r'^portfolio/(?P<slug>\w+)/$', Home.as_view(template_name="web/pages/portfolio_item.html"),name="portfolio"),
    url(r'^portfolio/', Home.as_view(template_name="web/pages/portfolio.html"),name="portfolio"),
)
