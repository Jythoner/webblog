from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()
from .views import IndexView, CategoryView, TagView, SearchView, ArticleDetailView, ArchiveView, LifeView, BookView, BookDetailView, ContactView
from .feed import LatestEntriesFeed


urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category>\w+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag>\w+)/$', TagView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view()),
    url(r'^detail/(?P<slug>\w+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^archive/$', ArchiveView.as_view(), name='archive'),
    url(r'^life/$', LifeView.as_view(), name='life'),
    url(r'^book/$', BookView.as_view(), name='book'),
    url(r'^book/detail/(?P<slug>\w+)/$', BookDetailView.as_view(), name='book_detail'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^rss/$', LatestEntriesFeed()),

]