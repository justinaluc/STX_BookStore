from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from books.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def get_api_spec(request):
    """gives a rigid specification data about required api project version"""
    spec = {
        "info": {
            "version": "2022.05.16"
            }
        }
    return Response(spec)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


