from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
from django.views.decorators.cache import cache_page
from .views import IndexView,CategoryView, TagView, SearchView, ArticleDetailView, ArchiveView, ContactView
from .feed import LatestEntriesFeed


urlpatterns = [

    url(r'^$', cache_page(15*60, cache='memcache')(IndexView.as_view()), name='index'),
    url(r'^category/(?P<category>\w+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag>\w+)/$', TagView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view()),
    url(r'^detail/(?P<slug>\w+)/$', cache_page(15*60, cache='memcache')(ArticleDetailView.as_view()), name='detail'),
    url(r'^archive/$', ArchiveView.as_view(), name='archive'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^rss/$', LatestEntriesFeed()),

]