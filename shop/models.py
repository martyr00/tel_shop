from django.db import models


class Telephone(models.Model):
    title = models.CharField(max_length=150, unique=True)
    brand = models.CharField(max_length=100)
    built_in_memory = models.CharField(max_length=100)
    price = models.BigIntegerField(null=False)

    diagonal_screen = models.FloatField(max_length=100)

    update_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
