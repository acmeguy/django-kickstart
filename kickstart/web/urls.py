from django.conf.urls import patterns, url
from views import Home, ContactUs, FanOut
from django.views.decorators.cache import cache_page

CACHE_PERIOD = 1*1

urlpatterns = patterns('',
    # Signup, signin and signout
    #url(r'^$', Home.as_view(template_name="web/pages/index.html"),name="home"),
    url(r'^$', cache_page(Home.as_view(template_name="web/pages/index.html"), CACHE_PERIOD), name='home'),
    url(r'^about_us/', cache_page(Home.as_view(template_name="web/pages/about_us.html"), CACHE_PERIOD), name='about'),
    url(r'^blog/(?P<slug>\w+)/$', Home.as_view(template_name="web/pages/blog_post.html"),name="blogpost"),
    url(r'^blog/', cache_page(Home.as_view(template_name="web/pages/blog_overview.html"), CACHE_PERIOD), name='blog'),
    url(r'^faq/', cache_page(Home.as_view(template_name="web/pages/faq_list.html"), CACHE_PERIOD), name='faq'),
    url(r'^pricing/', cache_page(Home.as_view(template_name="web/pages/pricing_overview.html"), CACHE_PERIOD), name='pricing'),
    url(r'^services/', cache_page(Home.as_view(template_name="web/pages/services_overview.html"), CACHE_PERIOD), name='services'),
    url(r'^testimonials/', cache_page(Home.as_view(template_name="web/pages/testimonials.html"), CACHE_PERIOD), name='testimonials'),
    url(r'^portfolio/', cache_page(Home.as_view(template_name="web/pages/portfolio.html"), CACHE_PERIOD), name='portfolio'),
    url(r'^portfolio/(?P<slug>\w+)/$', Home.as_view(template_name="web/pages/portfolio_item.html"),name="portfolio"),
    url(r'^contact/', ContactUs.as_view(),name="contact"),
    url(r'^video/', cache_page(Home.as_view(template_name="web/pages/video.html"), CACHE_PERIOD), name='video'),
    url(r'^send_message/', FanOut.as_view(),name="contact"),
)

