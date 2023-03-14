from django.db import models
from authors.models import Author
from shelf.models import Shelf
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_created = models.DateField()
    number_of_pages = models.IntegerField()
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
