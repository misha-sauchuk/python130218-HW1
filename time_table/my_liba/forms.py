from django.forms import ModelForm
from django import forms
from .models import Book, Author



class AddBook(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages', 'genre_id']


class AddAuthor(ModelForm):
    #years = forms.IntegerField(widget=forms.HiddenInput)  # make filed years invisibly

    class Meta:
        model = Author
        fields = ['name', 'surname', 'birthday', 'date_of_dearth', 'country_of_birth', 'book_id', 'years']

    # get date of birth and date of dearth and calculate the years of life
    def clean(self):
        cleaned_data = super().clean()
        birth = cleaned_data['birthday']
        dearth = cleaned_data['date_of_dearth']
        cleaned_data['years'] = dearth.year - birth.year
        return cleaned_data

    # change one filed, make name --> NAME
    def clean_name(self):
        name = self.cleaned_data['name']
        name = name.upper()
        return name


class UpdateBooks(ModelForm):
    class Meta:
        model = Book
        fields = ['pages']
