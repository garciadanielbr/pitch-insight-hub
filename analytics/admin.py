from django.contrib import admin
from .models import Player, Match, PlayerPerformance

admin.site.register(Player)
admin.site.register(Match)
admin.site.register(PlayerPerformance)