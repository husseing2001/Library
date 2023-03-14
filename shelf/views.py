from django.shortcuts import render
from rest_framework import generics
from .models import Shelf
from .serializers import ShelfSerializer


# Create your views here.
class ShelfList(generics.ListCreateAPIView):

    serializer_class = ShelfSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        serializer.save()

    def get_queryset(self, *args, **kwargs):
        return Shelf.objects.all()


class ShelfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    lookup_field = 'pk'
