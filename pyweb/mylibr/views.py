from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.db.models import Q
from django.views.generic import View

from .models import Author, Genre, Book
from .forms import BookModelForm, AuthorModelForm, GenreModelForm


def form_common(request, form, form_model):
    form_name = form_model(request.POST)
    if not form_name.is_valid():
        return HttpResponseBadRequest("Bad request")
    data = form_name.cleaned_data
    table = form(**data)  # Можно и так
    table.save()


def common_search(request, model, query):
    page_num = request.GET.get('page', 1)
    if query is not None:
        model_list = model.objects.filter(Q(name__icontains=query) |
                                          Q(id__icontains=query)).all()
    else:
        model_list = model.objects.all()
    p = Paginator(model_list, 13)
    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(1)
    return page


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, "index.html")


class BookView(View):

    def get(self, request):
        query = request.GET.get('q')
        page_num = request.GET.get('page', 1)
        if query is not None:
            book_list = Book.objects.filter(Q(name__icontains=query) |
                                            Q(author__name__icontains=query) |
                                            Q(genre__name__icontains=query) |
                                            Q(year__icontains=query)).all()
        else:
            book_list = Book.objects.all()
        p = Paginator(book_list, 10)
        try:
            page = p.page(page_num)
        except PageNotAnInteger:
            page = p.page(1)
        except EmptyPage:
            page = p.page(1)
        context = {'book_list': page}
        return render(request, 'search_results.html', context)


class BookEditView(View):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            author = Author.objects.all()
            genre = Genre.objects.all()
            return render(request, "edit.html", {"book": book,
                                                 "genre": genre,
                                                 "author": author}
                          )
        except Book.DoesNotExist:
            return render(request, 'search_results.html')

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.name = request.POST.get("name")
        book.year = request.POST.get("year")
        book.author_id = request.POST.get("author")
        book.genre_id = request.POST.get("genre")
        book.save()
        book_list = Book.objects.filter(id=book_id)
        context = {'book_list': book_list}
        return render(request, 'search_results.html', context)


class BookDeleteView(View):
    def post(self, request, book_id):
        try:
            Book.objects.get(id=book_id).delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Book.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")


class AuthorView(View):
    def get(self, request):
        query = request.GET.get('q1')
        page = common_search(request, Author, query)
        context = {'author_list': page}
        return render(request, 'change_author.html', context)


class AuthorEditView(View):
    def get(self, request, author_id):
        try:
            author = Author.objects.get(id=author_id)
            return render(request, "edit_author.html", {"author": author})
        except Author.DoesNotExist:
            return render(request, 'change_author.html')

    def post(self, request, author_id):
        author = Author.objects.get(id=author_id)
        author.name = request.POST.get("name")
        author.save()
        author_list = Author.objects.filter(id=author_id)
        context = {'author_list': author_list}
        return render(request, "change_author.html", context)


class AuthorDeleteView(View):
    def post(self, request, author_id):
        try:
            Author.objects.get(id=author_id).delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Author.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")


class GenreView(View):
    def get(self, request):
        query = request.GET.get('q2')
        page = common_search(request, Genre, query)
        context = {'genre_list': page}
        return render(request, 'change_genre.html', context)


class GenreEditView(View):
    def get(self, request, genre_id):
        try:
            genre = Genre.objects.get(id=genre_id)
            return render(request, "edit_genre.html", {"genre": genre})
        except Genre.DoesNotExist:
            return render(request, 'change_genre.html')

    def post(self, request, genre_id):
        genre = Genre.objects.get(id=genre_id)
        genre.name = request.POST.get("name")
        genre.save()
        genre_list = Genre.objects.filter(id=genre_id)
        context = {"genre_list": genre_list}
        return render(request, "change_genre.html", context)


class GenreDeleteView(View):
    def post(self, request, genre_id):
        try:
            Genre.objects.get(id=genre_id).delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Genre.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")


class BookFormView(View):
    @staticmethod
    def get(request):
        book_form = BookModelForm()
        return render(
            request,
            "change_book.html",
            context={
                "book_form": book_form,
            }
        )

    @staticmethod
    def post(request):
        try:
            form_common(request, Book, BookModelForm)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except Book.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")


class AuthorFormView(View):
    @staticmethod
    def get(request):
        return render(request, "change_book.html")

    @staticmethod
    def post(request):
        try:
            form_common(request, Author, AuthorModelForm)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Author.DoesNotExist:
            return HttpResponseNotFound("<h2>Author not found</h2>")


class GenreFormView(View):
    @staticmethod
    def get(request):
        return render(request, "change_book.html")

    @staticmethod
    def post(request):
        try:
            form_common(request, Genre, GenreModelForm)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Genre.DoesNotExist:
            return HttpResponseNotFound("<h2>Genre not found</h2>")
