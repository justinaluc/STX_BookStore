from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    external_id = models.CharField(max_length=60, null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    authors = models.ManyToManyField(Author, related_name="book_authors")
    published_year = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    acquired = models.BooleanField(default=False)
    thumbnail = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


