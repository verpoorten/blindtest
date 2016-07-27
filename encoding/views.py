from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from encoding.models import *
from django.core.urlresolvers import reverse
import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from dateutil.relativedelta import relativedelta
import datetime
from django.db import models

def page_not_found(request):
    return render(request,'page_not_found.html')


def access_denied(request):
    return render(request,'acces_denied.html')

def home(request):
    # return render(request, 'home.html',
    #                 {'livres': None})
    if request.user.is_authenticated():
        return render(request, 'home.html',
                        {'livres':   Livre.find_all_by_user(request.user),
                         'lectures': Lecture.find_all_by_user(request.user),
                         'emprunts' : Emprunt.find_emprunt_courant_by_user(request.user),
                         'en_locations' : Emprunt.find_locations(request.user)})
    else:
        return render(request, 'home.html',
                        {})
