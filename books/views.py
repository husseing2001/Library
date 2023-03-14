from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import permissions


# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def post(self, request, library_id):
    #     book = Book.objects.get(pk=library_id)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #  hus   serializer.save(book=book)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        user = self.request.user
        author = serializer.validated_data.get('author')
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('name') or None
        if description is None:
            description = name
        serializer.save(owner=user)

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return Book.objects.filter(owner=user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BookSerializer
    lookup_field = 'pk'
