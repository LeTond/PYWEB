from django import forms
from django.forms import Textarea

from .models import Book, Author, Genre, Year


class BookForm(forms.Form):
    name = forms.CharField(label='Name')
    author = forms.CharField(label='Author')
    genre = forms.CharField(label='Genre')
    year = forms.IntegerField(label='Year')


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        managed = False
        exclude = ["id"]
        widgets = {
            'name': Textarea(attrs={'cols': 54, 'rows': 1}),
        }


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        managed = False
        exclude = ["id"]
        widgets = {
            'name': Textarea(attrs={'cols': 40, 'rows': 1}),
        }


class GenreModelForm(forms.ModelForm):
    class Meta:
        model = Genre
        managed = False
        exclude = ["id"]
        widgets = {
            'name': Textarea(attrs={'cols': 40, 'rows': 1}),
        }


class YearModelForm(forms.ModelForm):
    class Meta:
        model = Year
        exclude = ["id"]