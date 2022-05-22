from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    external_id = models.CharField(max_length=60)
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name="book_authors")
    published_year = models.PositiveSmallIntegerField()
    acquired = models.BooleanField(default=False)
