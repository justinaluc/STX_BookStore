from django.shortcuts import render
from django.views.generic import ListView

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics

from .serializers import BookSerializer
from .models import Book


def home(request):
    return render(request, 'books/home.html')


class BookListView(ListView):
    """
    table view (not json format) of data in database
    """
    model = Book
    template = "book_list.html"


class BookList(generics.ListAPIView):
    """
    listing books with serializer which shows only related field representations (list of authors names)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    #to filter dates range use django-filter package: RangeFilter with RangeWidget
    filterset_fields = ['title', 'authors', 'published_year', 'acquired']


class BookCreate(generics.CreateAPIView):
    """
    create new instance of the book model
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    enable to show single instance of the book model, update it or delete it
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
