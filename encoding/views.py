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

def home(request):
    game = Game.find_open()
    gamesets = Gameset.find_by_game(game)
    return render(request, 'home.html',
                        {"game": game, "gamesets": gamesets})
