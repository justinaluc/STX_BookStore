from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template = "book_list.html"


def home_view(request):
    return render(request, 'books/home.html')