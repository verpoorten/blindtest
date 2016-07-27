from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.name

    def find_all():
        return Team.objects.all()

    @staticmethod
    def find_by_id(id):
        return Team.objects.get(pk=id)

class Category(models.Model):
    label = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.libelle


class Game(models.Model):
    name = models.CharField(max_length = 100,blank = False, null = False)

class Gameset(models.Model):
    game  = models.ForeignKey(Game)
    category  = models.ForeignKey(Category, blank = True, null = True)

class Result(models.Model):
    score = models.IntegerField(default=0)
    gameset  = models.ForeignKey(Gameset, blank = False, null = False)
    team  = models.ForeignKey(Team, blank = False, null = False)

class Answer(models.Model):
    answer = models.CharField(default=0)
    gameset  = models.ForeignKey(Gameset, blank = False, null = False)
