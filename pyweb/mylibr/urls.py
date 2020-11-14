from django.urls import path

from .views import IndexView, BookFormView, \
    AuthorFormView, GenreFormView, BookView, AuthorView, GenreView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('change_book/', BookFormView.as_view(), name='add-book'),

    path('change_book/change_author/', AuthorFormView.as_view(), name='add-author'),
    path('change_book/change_genre/', GenreFormView.as_view(), name='add-genre'),

    path('search/', BookView.as_view(), name='search_results'),
    path('author_form/', AuthorView.as_view(), name='change-author'),
    path('genre_form/', GenreView.as_view(), name='change-genre'),

    path('search_edit/<int:book_id>/', BookView.edit, name='edit-book'),
    path('search_delete/<int:book_id>/', BookView.delete, name='delete-book'),

    path('author_delete/<int:author_id>/', AuthorView.delete, name='delete-author'),
    path('author_edit/<int:author_id>/', AuthorView.edit, name='edit-author'),

    path('genre_delete/<int:genre_id>/', GenreView.delete, name='delete-genre'),
    path('genre_edit/<int:genre_id>/', GenreView.edit, name='edit-genre'),
]


