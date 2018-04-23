from django.contrib import admin
from .models import Author, Book, Edition, Publisher, Genre

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Edition)
admin.site.register(Publisher)
admin.site.register(Genre)