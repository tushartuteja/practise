from xapian import _queryparser_set_stopper
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from blog.models import Post
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test2.views.home', name='home'),
    url(r'^', ListView.as_view(queryset=Post.objects.all(), template_name="blog.html")),


)
