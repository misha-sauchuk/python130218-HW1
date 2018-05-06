from . import views
from django.urls import path


urlpatterns = [
    path('home', views.home_page, name='home'),
    path('mechanics/', views.mechanic, name='mechanics'),
    path('mechanics/<int:mechanic_id>', views.mechanic_info, name='mechanic_info'),
    path('months', views.months, name='months'),
    path('months/<int:month_id>', views.month_info, name='month_info'),
    path('timetable/', views.timetable, name='time_table'),
    path('create_timetable/', views.create_timetable, name='create_timetable'),
    path('add_mechanic/', views.add_mechanic, name='add_mechanic'),
    path('mod_mechanic/<int:mechanic_id>', views.modify_mechanic, name='mod_mechanic'),
    path('choose_month/', views.choose_month, name='choose_month'),
    path('mod_timetable/<int:timetable_id>', views.modify_timetable, name='mod_timetable'),


]

# path('books', views.books, name='books'),
# path('add_book_button', views.add_book_button, name='add_book_button'),
# path('add_author_button', views.add_author_button, name='add_author_button'),
# path('books/<int:book_id> ', views.book_info, name='book_info'),
# path('authors/', views.authors, name='authors'),
# path('author/<int:author_id>', views.author_info, name='author_info'),
# path('publishers/', views.publishers, name='publishers'),
# path('publishers/<int:publisher_id> ', views.publisher_info, name='publisher_info'),
# path('genres/', views.genres, name='genres'),
# path('genres/<int:genre_id> ', views.genre_info, name='genre_info'),
# path('add_book/', views.add_book, name='add_book'),
# path('add_author/', views.add_author, name='add_author'),
# path('books/<int:book_id>', views.update_book, name='update_book'),
# path('del_book/<int:book_id>', views.del_books, name='del_book'),
