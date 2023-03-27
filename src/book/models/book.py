from django.db import models
from acc.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='book_covers/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published=models.BooleanField(default=True)

    def __str__(self):
        return self.title