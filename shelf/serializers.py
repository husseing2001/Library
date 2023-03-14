from rest_framework import serializers
from books.serializers import BookSerializer
from .models import Shelf


class ShelfSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Shelf
        fields = ['name', 'books']

    def validate(self, attrs):
        name = attrs.get('name', '')

        if Shelf.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                {'name': 'Shelf exists'})
        return super().validate(attrs)
