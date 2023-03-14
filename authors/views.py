from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics


# Create your views here.
class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        serializer.save()

    def get_queryset(self, *args, **kwargs):
        return Author.objects.all()


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'
