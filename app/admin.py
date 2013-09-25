from django.contrib import admin

from app.models import Author, Book, Publisher

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)