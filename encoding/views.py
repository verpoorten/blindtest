from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from encoding.models import *
from django.core.urlresolvers import reverse
import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime
from django.db import models
from encoding.models import Game, Gameset
from operator import attrgetter
import operator

def home(request):
    game = Game.find_open()
    gamesets = Gameset.find_by_game(game)
    return render(request, 'home.html',
                        {"game": game,
                        "gamesets": gamesets,
                        "gameset": None,
                        "total_results": get_total_results(game)})


def result_encoding(request, result_id):
    result= Result.find_by_id(result_id)
    return render(request, 'result.html',
                        {"result": result})

def save_result(request, result_id):
    result= Result.find_by_id(result_id)
    score = request.POST.get('score')
    if score:
        result.score = score
        result.save()
    game = result.gameset.game
    gamesets = Gameset.find_by_game(game)
    return render(request, 'home.html',
                        {"game": result.gameset.game,
                         "gamesets": gamesets,
                         "gameset": result.gameset, "total_results": get_total_results(game)})

def change_tab_home(request, game_id=None):
    game = Game.find_by_id(game_id)
    gamesets = Gameset.find_by_game(game)
    return render(request, 'home.html',
                        {"game": game, "gamesets": gamesets, "total_results": get_total_results(game)})

def change_tab(request, gameset_id):
    gameset = Gameset.find_by_id(gameset_id)
    game = gameset.game
    gamesets = Gameset.find_by_game(game)
    return render(request, 'home.html',
                        {"game": game, "gamesets": gamesets, "gameset":gameset, "total_results": get_total_results(game)})

def view_scores(request, game_id):
    game = Game.find_by_id(game_id)
    results = Result.find_by_game(game.id)
    return render(request, 'score.html',
                        {"game": game, "total_results": get_total_results(game)})

def get_total_results(game):
    gamesets = Gameset.find_by_game(game)
    tt =[]
    for team in game.teams:
        tot = 0
        for gs in gamesets:
            results = Result.find_by_team_gameset(team, gs)
            for result in results:
                if result.score:
                    tot = tot + result.score
        team_total = TeamFinalTotalResult()
        team_total.team = team
        team_total.result = tot

        tt.append(team_total)

    return sorted(tt, key=attrgetter('result'), reverse=True)
    # return tt.sort(key=operator.attrgetter("result"), reverse=False)
    # return tt

class TeamFinalTotalResult:
    team = None
    result = 0
