from django.db import models
from author.models import Author
from catalog.models import Catalog


class Book(models.Model):
    name = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True)
    page = models.PositiveIntegerField(default=1)
    producer = models.CharField(max_length=180)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
