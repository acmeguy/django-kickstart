from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from tastypie.api import Api
from filebrowser.sites import site

admin.autodiscover()

v1_api = Api(api_name='v1')
#v1_api.register(EntryResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^kickstart/', include('kickstart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^accounts/', include('userena.urls')),
    url(r'^redis/status/', include('redis_cache.stats.urls', namespace='redis_cache')),

    #
    # Demo / reference content
    #
    url(r'^$', include('kickstart.web.urls')),
    #url(r'^$', 'kickstart.web.urls', name='web'),
)
