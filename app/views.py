from twisted.python import context
from django.views.generic import ListView, DetailView
from app.models import Publisher, Author, Book


class PublisherList(ListView):
    model = Publisher


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(publisher=context["publisher"])
        import ipdb
        ipdb.set_trace()


class AuthorList(ListView):
    model = Author


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book