from django.urls import path

from .views import IndexView, BookFormView, edit_book, delete_book, \
    edit_author, delete_author, edit_genre, delete_genre, edit_year, delete_year, \
    AuthorFormView, GenreFormView, YearFormView, search_author, search_genre, search_year, search_book

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('change_book/', BookFormView.as_view(), name='add-book'),
    path('change_book/change_author/', AuthorFormView.as_view(), name='add-author'),
    path('change_book/change_genre/', GenreFormView.as_view(), name='add-genre'),
    path('change_book/change_year/', YearFormView.as_view(), name='add-year'),

    path('search/', search_book, name='search_results'),
    path('author_form/', search_author, name='change-author'),
    path('genre_form/', search_genre, name='change-genre'),
    path('year_form/', search_year, name='change-year'),

    path('search/delete/<int:id>/', delete_book),
    path('search/edit/<int:id>/', edit_book),

    path('author_form/delete_author/<int:id>/', delete_author),
    path('author_form/edit_author/<int:id>/', edit_author),

    path('genre_form/delete_genre/<int:id>/', delete_genre),
    path('genre_form/edit_genre/<int:id>/', edit_genre),

    path('year_form/delete_year/<int:id>/', delete_year),
    path('year_form/edit_year/<int:id>/', edit_year),
]

