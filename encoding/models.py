from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.name

class Category(models.Model):
    label = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.label

class Game(models.Model):
    name = models.CharField(max_length = 100,blank = False, null = False)

    def __str__(self):
        return self.name
class Gameset(models.Model):
    game  = models.ForeignKey(Game)
    category  = models.ForeignKey(Category, blank = True, null = True)
    def __str__(self):
        return self.game

class Result(models.Model):
    score = models.IntegerField(default=0)
    gameset  = models.ForeignKey(Gameset, blank = False, null = False)
    team  = models.ForeignKey(Team, blank = False, null = False)

class Song(models.Model):
    interpreter = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    audio_file = models.FileField()
    play_time = models.IntegerField(default=5) # In seconds
    def __str__(self):
        return self.title
class Playlist(models.Model):
    gameset  = models.ForeignKey(Gameset)
    song  = models.ForeignKey(Song, blank = False, null = False)
