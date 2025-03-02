from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Cho phép null
    books = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Giỏ hàng của {self.user.username}"
