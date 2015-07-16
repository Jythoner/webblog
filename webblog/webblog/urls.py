from django.conf.urls import include, url, patterns
from django.contrib import admin
import settings
import xadmin
xadmin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'webblog.views.home', name='home'),
    url(r'', include('blog.url', namespace='blog')),
    url(r'^xadmin/', include(xadmin.site.urls)),
]

if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,
        }),
   )
