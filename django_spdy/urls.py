from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'world_flags.views.homepage', name='world_flags'),
)

urlpatterns += staticfiles_urlpatterns()