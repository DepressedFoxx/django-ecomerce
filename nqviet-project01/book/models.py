# models.py
from djongo import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()
    published_date = models.DateField(null=True, blank=True, default="2000-01-01")  # Giá trị mặc định

    objects = models.Manager()

    def __str__(self):
        return self.title