from django.db import models

class UserPlaylist(models.Model):
        songName = models.CharField(max_length=200)
        album = models.CharField(max_length=200)
        artist = models.CharField(max_length=200)
        duration = models.CharField(max_length=200)
        rating = models.CharField(max_length=1)


def __str__(self):
    return self.name

