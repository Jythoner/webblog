from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'webblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('blog.url'), name='blog'),
    url(r'^admin/', include(admin.site.urls)),
]