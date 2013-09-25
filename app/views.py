from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from app.forms import ContactForm
from app.models import Publisher, Author, Book


class PublisherList(ListView):
    model = Publisher


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Finding publisher`s books
        context['book_list'] = Book.objects.filter(publisher=context["publisher"])
        return context


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author

    def get_object(self, queryset=None):
        object = super(AuthorDetail, self).get_object()
        # Update last accessed time
        object.last_accessed = timezone.now()
        object.save()
        return object

class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()

        return super(ContactView, self).form_valid(form)
