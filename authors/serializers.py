from rest_framework import serializers
from books.models import Book
from .models import Author
from books.serializers import BookSerializer


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # user = UserSerializer(read_only = True)
        fields = ['name', 'books']

    def validate(self, attrs):
        name = attrs.get('name', '')

        if Author.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                {'name': 'Author exists'})
        return super().validate(attrs)
