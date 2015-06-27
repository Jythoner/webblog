from django.conf.urls import url
from .views import IndexView, ArticleDetailView, CategoryView, TagView, SearchView


urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category>\w+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag>\w+)/$', TagView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view()),
    url(r'^detail/(?P<en_title>\w+)/$', ArticleDetailView.as_view(), name='detail'),

]