from django.shortcuts import render
from .models import Author, Book, Publisher, Edition, Genre

# Create your views here.


def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', context={'books':books})


def book_info(requst, book_id):
    book = Book.objects.get(id=book_id)
    return render(requst, 'book_info.html', context={'book_info':book})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', context={'authors':authors})


def author_info(request, author_id):
    print('--------------------------------', author_id)
    author = Author.objects.get(id=author_id)
    return render(request, 'author_info.html', context={'author_infor':author})


def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers.html', context={'publishers':publishers})


def publisher_info(request, publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)
    return render(request, 'publisher_info.html', context={'publisher_infor':publisher})


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', context={'genres':genres})


def genre_info(request, genre_id):
    genre = Author.objects.get(id=genre_id)
    return render(request, 'genre_info.html', context={'genres_infor':genre})