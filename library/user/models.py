from django.db import models
from community.models import Library

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=64)
    author=models.CharField(max_length=64)

    library=models.ManyToManyField(Library,related_name="books")

    objects = models.Manager()

    def __str__(self):
        return f"{self.title} by {self.author}"