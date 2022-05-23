from rest_framework import serializers
from books.models import Book, Author


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'external_id', 'title', 'authors', 'acquired', 'published_year')
        depth = 1