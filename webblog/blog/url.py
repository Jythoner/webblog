from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
from .views import IndexView,CategoryView, TagView, SearchView, ArticleDetailView, ArchiveView, ArticleDayView
from .feed import LatestEntriesFeed


urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category>\w+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag>\w+)/$', TagView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view()),
    url(r'^detail/(?P<slug>\w+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^archive/$', ArchiveView.as_view(), name='archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',  ArticleDayView.as_view(),  name="archive_day"),
    url(r'^rss/$', LatestEntriesFeed()),

]