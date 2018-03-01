from django.db import models

class books(models.Model):
    book_name = models.CharField(max_length=100, null=False)
    isbn = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.book_name

class cart(models.Model):
    isbn = models.CharField(max_length=100, null=False)
    book_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.book_name