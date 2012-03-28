__author__ = 'jijing'

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('polls.views',
    # Patterns for poll app
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
