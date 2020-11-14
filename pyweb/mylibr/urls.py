from django.urls import path

from .views import IndexView, BookFormView, \
    AuthorFormView, GenreFormView, BookView, AuthorView, \
    GenreView, BookEditView, BookDeleteView, AuthorDeleteView, \
    AuthorEditView, GenreDeleteView, GenreEditView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('change_book/', BookFormView.as_view(), name='add-book'),

    path('change_book/change_author/', AuthorFormView.as_view(), name='add-author'),
    path('change_book/change_genre/', GenreFormView.as_view(), name='add-genre'),

    path('search/', BookView.as_view(), name='search_results'),
    path('author_form/', AuthorView.as_view(), name='change-author'),
    path('genre_form/', GenreView.as_view(), name='change-genre'),

    path('search_edit/<int:book_id>/', BookEditView.as_view(), name='edit-book'),
    path('search_delete/<int:book_id>/', BookDeleteView.as_view(), name='delete-book'),

    path('author_delete/<int:author_id>/', AuthorDeleteView.as_view(), name='delete-author'),
    path('author_edit/<int:author_id>/', AuthorEditView.as_view(), name='edit-author'),

    path('genre_delete/<int:genre_id>/', GenreDeleteView.as_view(), name='delete-genre'),
    path('genre_edit/<int:genre_id>/', GenreEditView.as_view(), name='edit-genre'),
]


