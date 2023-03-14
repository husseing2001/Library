from rest_framework import serializers
from .models import Book
from authors.models import Author
from shelf.models import Shelf


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    shelf = serializers.PrimaryKeyRelatedField(queryset=Shelf.objects.all())

    class Meta:
        model = Book

        fields = [
            'id',
            'name',
            'date_created',
            'number_of_pages',
            'description',
            'author',
            'shelf'
        ]
