from rest_framework import serializers
from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    #do not require author id if exists when update Book instance with nested author serializer
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Author
        fields = ['id', 'name']
        read_only_fields = ('id',)
        write_only_fields = ('name',)

    def to_representation(self, value):
        return f'{value.name}'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True) #serializers.StringRelatedField is read_only

    class Meta:
        model = Book
        fields = ['id', 'external_id', 'title', 'authors', 'acquired', 'published_year', 'thumbnail']

    # def create(self, validated_data):
    #     """
    #     create new model instance
    #     """
    #     authors = validated_data.pop('authors', [])
    #     book = Book.objects.create(**validated_data)
    #     for author in authors:
    #         book.authors.add(author)
    #     return book
    # #
    # def update(self, instance, validated_data):
    #     """
    #     update model instance with validated data
    #     """
    #     authors = validated_data.pop('authors')
    #     for author in authors:
    #         name = author.get('name')
    #         author_choice = Author.objects.get(name)
    #         instance.authors.add(author_choice)
    #     return instance
