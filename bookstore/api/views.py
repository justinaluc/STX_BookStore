from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from books.models import Book
from .serializers import BookSerializer


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def get_api_spec(request):
    spec = {
        "info": {
            "version": "2022.05.16"
            }
        }
    return Response(spec)
