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
