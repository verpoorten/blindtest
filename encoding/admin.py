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
from django.contrib import admin
from .models import *

#
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Gameset, GamesetAdmin)
admin.site.register(Playlist)
admin.site.register(Result)
admin.site.register(Song)
admin.site.register(Team)
