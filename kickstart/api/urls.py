# coding=utf-8
import django.conf.urls
from rest_framework.urlpatterns import format_suffix_patterns
from kickstart.api.views import UserList, UserDetail, GroupList, GroupDetail

urlpatterns = django.conf.urls.patterns('kickstart.api.views',
    django.conf.urls.url(r'^$', 'api_root'),
    django.conf.urls.url(r'^users/$', UserList.as_view(), name='user-list'),
    django.conf.urls.url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    django.conf.urls.url(r'^groups/$', GroupList.as_view(), name='group-list'),
    django.conf.urls.url(r'^groups/(?P<pk>\d+)/$', GroupDetail.as_view(), name='group-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += django.conf.urls.patterns('',
    django.conf.urls.url(r'^api-auth/', django.conf.urls.include('rest_framework.urls', namespace='rest_framework'))
)
