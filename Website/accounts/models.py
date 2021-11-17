from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):

    name = models.CharField(max_length=256)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    platform = models.ForeignKey(Platform, null=True, on_delete=models.SET_NULL)
    release_date = models.DateField(null=True)
    score = models.FloatField(default=0, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    SCORE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)
    score = models.IntegerField(choices=SCORE)
    comments = models.CharField(max_length=1024, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.game.name + '/' + self.user.username
