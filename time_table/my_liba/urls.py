from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='books'),
    path('books/', views.books, name='books'),
    path('add_book_button', views.add_book_button, name='add_book_button'),
    path('add_author_button', views.add_author_button, name='add_author_button'),
    path('books/<int:book_id> ', views.book_info, name='book_info'),
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>', views.author_info, name='author_info'),
    path('publishers/', views.publishers, name='publishers'),
    path('publishers/<int:publisher_id> ', views.publisher_info, name='publisher_info'),
    path('genres/', views.genres, name='genres'),
    path('genres/<int:genre_id> ', views.genre_info, name='genre_info'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_author/', views.add_author, name='add_author'),

]
