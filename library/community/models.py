from django.db import models

# Create your models here.
CHOICES = [
    ("private","Private"),("public","Public")
]

class Library(models.Model):
    title=models.CharField(max_length=64)
    description=models.CharField(max_length=64)
    privacy=models.CharField(choices=CHOICES, default="private",max_length=64)

    objects=models.Manager()

    def __str__(self):
        return self.title

'''
class Book(models.Model):
    title=models.CharField(max_length=64)
    author=models.CharField(max_length=64)

    objects = models.Manager()

    def __str__(self):
        return f"{self.title} by {self.author}"
'''