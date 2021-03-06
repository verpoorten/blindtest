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
                        {"game": game,
                         "gamesets": gamesets,
                         "gameset":gameset,
                         "total_results": get_total_results(game)})

def view_scores(request, game_id):
    game = Game.find_by_id(game_id)
    results = Result.find_by_game(game.id)
    return render(request, 'score.html',
                        {"game": game, "total_results": get_total_results(game)})

def results_encoding(request, a_gameset_id):
    results = Result.find_by_gameset(a_gameset_id)
    gameset = Gameset.find_by_id(a_gameset_id)
    teams = Team.find_teams_by_game(gameset.game)
    for tm in teams:
        found = False
        for r in results:
            if r.team.id == tm.id:
                found = True
                break
        if not found:
            new_result = Result()
            new_result.team = tm
            new_result.score = 0
            new_result.gameset = gameset
            new_result.save()
    results = Result.find_by_gameset(a_gameset_id)
    return render(request, 'results.html', {"results": results})

def get_total_results(game=None):
    gamesets = Gameset.find_by_game(game)
    tt =[]
    if game:
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

def result_save(request):
    print('result_save')
    result_id = request.GET['res_id']
    score = request.GET['result']
    result= Result.find_by_id(result_id)
    result.score = score
    result.save()
    return None

def save_results(request):
    gameset = None
    for key, value in request.POST.items():
        print(key, value)
        if(key.startswith('result_id_')):
            result_id = key.replace('result_id_', '')
            result= Result.find_by_id(result_id)
            result.score = int(value)
            result.save()
            if gameset is None:
                gameset = result.gameset
    return change_tab(request, gameset.id)

def display_player_all(request, game_id):
    game = Game.find_by_id(game_id)
    return render(request, 'all_scores.html', {"total_results": get_total_results(game), "game": game})

def results_view(request, a_gameset_id):
    results = Result.find_by_gameset(a_gameset_id)
    gameset = Gameset.find_by_id(a_gameset_id)
    teams = Team.find_teams_by_game(gameset.game)
    for tm in teams:
        found = False
        for r in results:
            if r.team.id == tm.id:
                found = True
                break
        if not found:
            new_result = Result()
            new_result.team = tm
            new_result.score = 0
            new_result.gameset = gameset
            new_result.save()
    results = Result.find_by_gameset(a_gameset_id)
    return render(request, 'results_full.html', {"results": results,
                                                 "gameset": gameset})


def answers_view(request, a_gameset_id):
    gameset = Gameset.find_by_id(a_gameset_id)

    results = Result.find_by_gameset(a_gameset_id)
    return render(request, 'answers_full.html', { "gameset": gameset})


class TeamFinalTotalResult:
    team = None
    result = 0
