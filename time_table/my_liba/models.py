from django.db import models

# Create your models here.


class Genre(models.Model):
    genre = models.CharField(max_length=250, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=250)
    pages = models.IntegerField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    birthday = models.DateField()
    country_of_birth = models.CharField(max_length=250)
    book_id = models.ManyToManyField(Book)


class Publisher(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    author_id = models.ManyToManyField(Author)


class Edition(models.Model):
    date = models.DateField()
    amount = models.IntegerField()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)