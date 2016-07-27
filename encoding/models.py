from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Team(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.name

class Category(models.Model):
    label = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.label

class Game(models.Model):
    OPEN_STATUS = (
        ('CLOSE', _('close')),
        ('OPEN', _('open'))
    )
    name = models.CharField(max_length = 100,blank = False, null = False)
    open_status = models.CharField(max_length=20, choices=OPEN_STATUS, default='CLOSE', blank=False, null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def find_open():
        games= Game.objects.filter(open_status='OPEN')
        if games:
            print(games[0].name)
            return games[0]

class Gameset(models.Model):
    game  = models.ForeignKey(Game)
    category  = models.ForeignKey(Category, blank = True, null = True)

    def __str__(self):
        return self.game.name

    @staticmethod
    def find_by_game(a_game):
        return Gameset.objects.filter(game=a_game)

    @property
    def playlist(self):
        playlists = Playlist.objects.filter(gameset=self)
        if playlists:
            return playlists[0]

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

    def __str__(self):
        if self.song:
            return self.song.title
        else:
            return ""
