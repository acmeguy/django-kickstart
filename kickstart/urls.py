# coding=utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^accounts/', include('userena.urls')),
    #url(r'^redis/status/', include('redis_cache.stats.urls', namespace='redis_cache')),
    url(r'^search/', include('haystack.urls')),

    #
    # Demo / api content
    #
    #url(r'^api/', include('kickstart.api.urls', namespace='rest_api')),
    url(r'^api/', include('kickstart.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #
    # Proxy
    #
    url(r'^extmedia/(?P<url>.*)$', 'httpproxy.views.proxy'),

    #
    # Demo / reference content
    #
    url(r'^', include('kickstart.web.urls',namespace='web')),

)

#Gunicorn development settings which forces it to serve static files.
if settings.DEBUG:
    urlpatterns.append(url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT, 'show_indexes':True}))
