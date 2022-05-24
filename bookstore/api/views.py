from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend

from books.models import Book
from .serializers import BookSerializer, BookListSerializer


@api_view(['GET'])
def get_api_spec(request):
    """gives a rigid specification data about required api project version"""
    spec = {
        "info": {
            "version": "2022.05.16"
            }
        }
    return Response(spec)


class BookList(generics.ListAPIView):
    """
    listing books with serializer which shows only related field representations
    """
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'authors', 'published_year', 'acquired']


class BookCreate(generics.CreateAPIView):
    """
    create new instance of the book model
    """
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    enable to show single instance of the book model, update it or delete it
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
