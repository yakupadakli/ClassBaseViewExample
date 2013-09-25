from django.conf.urls import patterns, url

from app.views import PublisherList, AuthorList, BookList, BookDetail

urlpatterns = patterns('',
    url(r'^publishers/$', PublisherList.as_view(template_name="publisher_list.html")),
    url(r'^authors/$', AuthorList.as_view(template_name="author_list.html")),
    url(r'^books/$', BookList.as_view(template_name="book_list.html")),
    url(r'^book/(?P<pk>\d+)/$', BookDetail.as_view(template_name="book_detail.html")),
)