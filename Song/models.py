from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Genre(models.Model):
    type = models.CharField(max_length=100)


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100)
    published_date = models.DateField()

    genres = models.ManyToManyField(Genre, related_name="songs")

    def __str__(self):
        return self.song_name


class Collection(models.Model):
    collection_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    songs = models.ManyToManyField(Song, related_name="songs")
