from django.db import models


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} || id: {self.id}"

    class Meta:
        ordering = ["name"]


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} || id: {self.id}"

    class Meta:
        ordering = ["name"]


# class Year(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.IntegerField(blank=True)
#
#     def __str__(self):
#         return f"{self.name} || id: {self.id}"
#
#     class Meta:
#         ordering = ["name"]


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, related_name='genre', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id} -- {self.name} // {self.author.name} // {self.genre.name} // {self.year.name}"

    class Meta:
        ordering = ["name"]