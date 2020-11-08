from django.contrib import admin
from .models import Author, Genre, Year, Book


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Year)
admin.site.register(Book)

