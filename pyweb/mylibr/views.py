from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.db.models import Q
from django.views.generic import View
from html import escape

from .models import Author, Genre, Year, Book
from .forms import BookModelForm, AuthorModelForm, GenreModelForm, YearModelForm


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class BookFormView(View):
    def get(self, request):
        book_form = BookModelForm()
        return render(
            request,
            "change_book.html",
            context={
                "book_form": book_form,
            }
        )

    def post(self, request):
        try:
            if request.method == "POST":
                book_form = BookModelForm(request.POST)
                if not book_form.is_valid():
                    return HttpResponseBadRequest("Bad Request")
                data = book_form.cleaned_data
                book = Book(**data)
                book.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse("Invalid data")

        except Book.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")


class AuthorFormView(View):
    def get(self, request):
        return render(request, "change_book.html")

    def post(self, request):
        try:
            if request.method == "POST":
                author_form = AuthorModelForm(request.POST)
                if not author_form.is_valid():
                    return HttpResponseBadRequest("Bad request")
                data = author_form.cleaned_data
                author = Author(**data)  # Можно и так
                author.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse("Invalid data")

        except Author.DoesNotExist:
            return HttpResponseNotFound("<h2>Author not found</h2>")


class GenreFormView(View):
    def get(self, request):
        return render(request, "change_book.html")

    def post(self, request):
        try:
            if request.method == "POST":
                genre_form = GenreModelForm(request.POST)
                if not genre_form.is_valid():
                    return HttpResponseBadRequest("Bad request")
                data = genre_form.cleaned_data
                genre = Genre(**data)  # Можно и так
                genre.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse("Invalid data")

        except Genre.DoesNotExist:
            return HttpResponseNotFound("<h2>Genre not found</h2>")


class YearFormView(View):
    def get(self, request):
        return render(request, "change_book.html")

    def post(self, request):
        try:
            if request.method == "POST":
                year_form = YearModelForm(request.POST)
                if not year_form.is_valid():
                    return HttpResponseBadRequest("The Year must be integer")
                data = year_form.cleaned_data
                year = Year(**data)  # Можно и так
                year.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse("Invalid data")
        except Year.DoesNotExist:
            return HttpResponseNotFound("<h2>Year not found</h2>")


def search_book(request):
    query = request.GET.get('q')
    page_num = request.GET.get('page', 1)
    if query is not None:
        book_list = Book.objects.filter(Q(name__icontains=query) |
                                        Q(author__name__icontains=query) |
                                        Q(genre__name__icontains=query) |
                                        Q(year__name__icontains=query)).all()
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


def search_author(request):
    query = request.GET.get('q1')
    page_num = request.GET.get('page', 1)
    if query is not None:
        author_list = Author.objects.filter(name__icontains=query).all()
    else:
        author_list = Author.objects.all()
    p = Paginator(author_list, 18)
    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(1)
    context = {'author_list': page}
    return render(request, 'change_author.html', context)


def search_genre(request):
    query = request.GET.get('q2')
    page_num = request.GET.get('page', 1)
    if query is not None:
        genre_list = Genre.objects.filter(name__icontains=query).all()
    else:
        genre_list = Genre.objects.all()
    p = Paginator(genre_list, 18)
    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(1)
    context = {'genre_list': page}
    return render(request, 'change_genre.html', context)


def search_year(request):
    query = request.GET.get('q3')
    page_num = request.GET.get('page', 1)
    if query is not None:
        year_list = Year.objects.filter(name__icontains=query).all()
    else:
        year_list = Year.objects.all()
    p = Paginator(year_list, 18)
    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(1)
    context = {'year_list': page}
    return render(request, 'change_year.html', context)


def edit_book(request, id):
    try:
        book = Book.objects.get(id=id)
        author = Author.objects.all()
        genre = Genre.objects.all()
        year = Year.objects.all()

        if request.method == "POST":
            book.name = request.POST.get("name")
            book.author_id = request.POST.get("author")
            book.genre_id = request.POST.get("genre")
            book.year_id = request.POST.get("year")
            book.save()
            return render(request, "search_results.html")
        else:
            return render(request, "edit.html", {"book": book,
                                                 "genre": genre,
                                                 "author": author,
                                                 "year": year}
                          )
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")


def edit_author(request, id):
    try:
        author = Author.objects.get(id=id)
        if request.method == "POST":
            author.name = request.POST.get("name")
            author.save()
            return render(request, "change_author.html")
        else:
            return render(request, "edit_author.html", {"author": author})
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Author not found</h2>")


def edit_genre(request, id):
    try:
        genre = Genre.objects.get(id=id)
        if request.method == "POST":
            genre.name = request.POST.get("name")
            genre.save()
            return render(request, "change_genre.html")
        else:
            return render(request, "edit_genre.html", {"genre": genre})
    except Genre.DoesNotExist:
        return HttpResponseNotFound("<h2>Genre not found</h2>")


def edit_year(request, id):
    try:
        year = Year.objects.get(id=id)
        if request.method == "POST":
            year.name = request.POST.get("name")
            # if not isinstance(year.name, int):
            #     return HttpResponseBadRequest("The Year must be integer")
            year.save()
            return render(request, "change_year.html")
        else:
            return render(request, "edit_year.html", {"year": year})
    except Year.DoesNotExist:
        return HttpResponseNotFound("<h2>Year not found</h2>")


def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")


def delete_author(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Author not found</h2>")


def delete_genre(request, id):
    try:
        genre = Genre.objects.get(id=id)
        genre.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Genre.DoesNotExist:
        return HttpResponseNotFound("<h2>Genre not found</h2>")


def delete_year(request, id):
    try:
        year = Year.objects.get(id=id)
        year.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Year.DoesNotExist:
        return HttpResponseNotFound("<h2>Year not found</h2>")





# class SearchYearView(ListView):
#     model = Year
#     template_name = 'change_year.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q3')
#         if query is not None:
#             year_list = Year.objects.filter(name__icontains=query).all().order_by('name')
#             return year_list
#         else:
#             year_list = Year.objects.all()
#         return year_list


# class SearchGenreView(ListView):
#     model = Genre
#     template_name = 'change_genre.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q2')
#         if query is not None:
#             genre_list = Genre.objects.filter(name__icontains=query).all().order_by('name')
#             return genre_list
#         else:
#             genre_list = Genre.objects.all()
#         return genre_list


# class SearchAuthorView(ListView):
#     model = Author
#     template_name = 'change_author.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q1')
#         if query is not None:
#             author_list = Author.objects.filter(name__icontains=query).all()
#             return author_list
#         else:
#             author_list = Author.objects.all()
#             return author_list


# class SearchResultView(ListView):
#     model = Book
#     template_name = 'search_results.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query is not None:
#             object_list = Book.objects.filter(Q(name__icontains=query) |
#                                               Q(author__name__icontains=query) |
#                                               Q(genre__name__icontains=query) |
#                                               Q(year__name__icontains=query)).all()
#             return object_list
#         else:
#             object_list = Book.objects.all()
#             return object_list



# class AddGenreFormView(View):
#     def get(self, request):
#         genre_form = GenreModelForm()
#         return render(
#             request,
#             "change_genre.html",
#             context={
#                 "genre_form": genre_form,
#             }
#         )
#
#     def post(self, request):
#         genre_form = GenreModelForm(request.POST)
#         if not genre_form.is_valid():
#             return HttpResponseBadRequest("Bad Request")
#         genre = genre_form.save()
#         return HttpResponse(escape(f"Добавлена автор: {genre.name}"))



# class TestView(View):
#
#     @staticmethod
#     @transaction.atomic
#     def create_author(name):
#         a = Author(name=name)
#         a.save()
#
#     @staticmethod
#     @transaction.atomic
#     def create_genre(name):
#         g = Genre(name=name)
#         g.save()
#
#     @staticmethod
#     @transaction.atomic
#     def create_year(name):
#         y = Year(name=name)
#         y.save()
#
#     @staticmethod
#     @transaction.atomic
#     def create_lib(list_):
#         i_list = []
#         for i in range(len(list_)):
#             book = list_[i][0]
#             author = Author.objects.get(name=list_[i][1])
#             genre = Genre.objects.get(name=list_[i][2])
#             year = Year.objects.get(name=list_[i][3])
#             i = Book(name=book,
#                      author_id=author.id,
#                      genre_id=genre.id,
#                      year_id=year.id)
#             i_list.append(i)
#         print(i_list)
#         Book.objects.bulk_create(i_list)
#
#     @staticmethod
#     @transaction.atomic
#     def delete_from_authors(name):
#         for auth in Author.objects.all().filter(name=name):
#             auth.delete()
#
#     @staticmethod
#     @transaction.atomic
#     def write_to_table(from_document, table_name):
#         with open(from_document, 'r', encoding='utf-8') as f:
#             file = f.read()
#         file_s = file.split('\n')
#         for f in file_s:
#             if f != '':
#                 table_name(f.strip())
#
#     def write_to_table_years(self, from_, to_):
#         for i in range(from_, to_ + 1):
#             self.create_year(i)
#
#     # def get(self, request):
#     #     with transaction.atomic():
#     # self.write_to_table('Genre.txt', self.create_genre)
#     # self.write_to_table('Author.txt', self.create_author)
#     # self.write_to_table_years(1452, 2020)
#     # self.create_author("Jack London")
#     # self.delete_from_authors('Jack London')
#     # self.create_genre("Play")
#     # self.find_book_in_lib(249)
#
#     # list_ = [["Lady Windermere's Fan", 'Wilde, Oscar', 'Play', 1892],
#     #          ["The Importance of Being Earnest ", 'Wilde, Oscar', 'Play', 1895],
#     #          ["The Picture of Dorian Gray", 'Wilde, Oscar', 'Novel', 1890],
#     #          ["An Ideal Husband", 'Wilde, Oscar', 'Play', 1895],
#     #          ["The Sea-Wolf", 'London, Jack', 'Novel', 1904],
#     #          ["Martin Eden", 'London, Jack', 'Novel', 1909],
#     #          ["White Fang ", 'London, Jack', 'Novel', 1906],
#     #          ["The Little Lady of the Big House", 'London, Jack', 'Novel', 1916]]
#
#     # self.create_lib(list_)
#     # return render(request, "change_form.html")
