from django.db import models
from apps.core.models import TimeBase


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=255)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.nickname


class Book(TimeBase):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,  null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    times_read = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title
