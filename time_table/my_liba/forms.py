from django.forms import ModelForm
from .models import Book, Author
from datetime import datetime


class AddBook(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages', 'genre_id']
        # model = Author
        # fields = ['Author.all']


class AddAuthor(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'birthday', 'date_of_dearth', 'country_of_birth', 'book_id']

        def clean_country_of_birth(self):
            country_of_birth = self.cleaned_data['country_of_birth']
            if country_of_birth == 'Россия':
                country_of_birth = 'Русь'
                return country_of_birth
            raise ValueError

        # def clean(self):
        #     years = self.cleaned_data['years']
        #     birthday = self.cleaned_data['birthday']
        #     date_of_dearth = self.cleaned_data['date_of_dearth']
        #     years = date_of_dearth.datetime.years - birthday.datetime.years
        #     return years

        def save(self):
            author = Author(**self.cleaned_data)
            author.save()
            return author