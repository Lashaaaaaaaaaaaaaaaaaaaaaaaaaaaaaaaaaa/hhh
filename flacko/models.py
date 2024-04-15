from django.db import models


class Lord(models.Model):
    name = models.CharField(max_length=100, default="name")
    surname = models.CharField(max_length=100, default="surname")
    personal_thoughts = models.TextField()


class Jordy(models.Model):
    title = models.CharField(max_length=100, default="Title")
    description = models.TextField()
    lord = models.ForeignKey(Lord, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, default="Genre")
    release_date = models.DateTimeField()
    personal_thoughts = models.TextField()
