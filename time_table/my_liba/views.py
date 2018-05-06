from django.shortcuts import render
from .models import Author, Book, Publisher, Edition, Genre
from .forms import AddBook, AddAuthor, UpdateBooks
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', context={'books': books})


def book_info(requst, book_id):
    book = Book.objects.get(id=book_id)
    return render(requst, 'book_info.html', context={'book_info': book})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', context={'authors': authors})


def author_info(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'author_info.html', context={'author_info': author})


def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers.html', context={'publishers': publishers})


def publisher_info(request, publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)
    return render(request, 'publisher_info.html', context={'publisher_info': publisher})


def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', context={'genres': genres})


def genre_info(request, genre_id):
    genre = Author.objects.get(id=genre_id)
    return render(request, 'genre_info.html', context={'genres_info': genre})


def add_book(request):
    form_book = AddBook()
    if request.method == 'POST':
        form_book = AddBook(request.POST)
        if form_book.is_valid():
            form_book.save()
            return HttpResponseRedirect('/liba/books')
    return render(request, 'add_book.html', context={'add_book': form_book})


def add_author(request):
    form = AddAuthor()
    if request.method == 'POST':
        form = AddAuthor(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/liba/books')
    return render(request, 'add_author.html', context={'add_author': form})


def add_book_button(request):
    return HttpResponseRedirect('/liba/add_book')


def add_author_button(request):
    return HttpResponseRedirect('/liba/add_author')

def del_books(request, book_id):
    book = Book.objects.get(id=book_id).delete()
    return render(request, 'del_book.html', context={'del_book':book})


def home_page(request):
    return HttpResponse('liba/books')


def update_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        pages = UpdateBooks(request.POST, instance=book)
        if pages.is_valid():
            pages.save()
            return HttpResponseRedirect('/liba/books')

    pages = UpdateBooks(instance=book)
    return render(request, 'update_pages.html', context={'update_book': pages})


