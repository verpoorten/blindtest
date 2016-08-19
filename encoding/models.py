##############################################################################
#
#    Blindtest it's an application to organize Blindtest
#
#    Copyright (C) 2016-2017 Verpoorten Leïla
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin


class Game(models.Model):
    OPEN_STATUS = (
        ('CLOSE', _('close')),
        ('OPEN', _('open'))
    )
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    open_status = models.CharField(max_length=20, choices=OPEN_STATUS, default='CLOSE', blank=False, null=False)

    def __str__(self):
        return self.name

    @property
    def teams(self):
        return Team.objects.filter(game=self)


    @staticmethod
    def find_by_id(game_id):
        return Game.objects.get(pk=game_id)

    @staticmethod
    def find_open():
        games= Game.objects.filter(open_status='OPEN')
        if games:
            return games[0]


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    game  = models.ForeignKey(Game, blank=False, null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def find_teams_by_game(a_game):
        return Team.objects.filter(game=a_game)


class Category(models.Model):
    label = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.label


class GamesetAdmin(admin.ModelAdmin):
    list_display = ('game','category')
    search_fields = ['game','category']
    list_filter = ('game','category')


class Gameset(models.Model):
    game = models.ForeignKey(Game)
    category = models.ForeignKey(Category, blank=True, null=True)

    def __str__(self):
        ch = self.game.name
        if self.category:
            ch += " - " + self.category.label
        return ch

    @staticmethod
    def find_by_id(a_gameset_id):
        return Gameset.objects.get(pk=a_gameset_id)

    @staticmethod
    def find_by_game(a_game):
        return Gameset.objects.filter(game=a_game)

    @property
    def playlist(self):
        return Playlist.objects.filter(gameset=self)

    @property
    def results(self):
        return Result.objects.filter(gameset=self)


class Result(models.Model):
    score = models.IntegerField( blank=True, null=True)
    gameset  = models.ForeignKey(Gameset, blank=False, null=False)
    team  = models.ForeignKey(Team, blank=False, null=False)

    @staticmethod
    def find_by_id(an_id):
        return Result.objects.get(pk=an_id)

    @staticmethod
    def find_by_game(an_game):
        return Result.objects.filter(gameset__game=an_game)

    @staticmethod
    def find_by_gameset( a_gameset):
        return Result.objects.filter(gameset=a_gameset)

    @staticmethod
    def find_by_team_gameset(a_team, a_gameset):
        return Result.objects.filter(team=a_team,gameset=a_gameset)


class Style(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(models.Model):
    interpreter = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='songs/')
    play_time = models.IntegerField(default=10)  # In seconds
    description = models.CharField(max_length=255, blank=True, null=True)
    style = models.ForeignKey(Style, null=True, blank=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    gameset = models.ForeignKey(Gameset)
    song = models.ForeignKey(Song, blank=False, null=False)

    def __str__(self):
        if self.song:
            return self.song.title
        else:
            return ""
