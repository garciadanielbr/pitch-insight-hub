from django.db import connection
from rest_framework import viewsets, views

from .models import (
    League, 
    Season, 
    Team, 
    Fixture,
    )
from .serializers import (
    LeagueSerializer,
    SeasonSerializer,
    TeamSerializer,
    FixtureSerializer,
)


class LeagueView(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class SeasonView(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class FixtureView(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
