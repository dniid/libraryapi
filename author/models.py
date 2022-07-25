from django.db import models


class Author(models.Model):
    name = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
