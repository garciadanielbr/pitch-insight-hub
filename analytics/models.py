from django.db import models
from django.db.models import Avg, Sum

class League(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'leagues'

class Season(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    year = models.IntegerField()
    fetch_required = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.year) + ' - ' + str(self.league.name)
    
    class Meta:
            db_table = 'seasons'
class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
            db_table = 'teams'
class SeasonTeam(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
            db_table = 'season_teams'
class Fixture(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    round = models.CharField(max_length=100)
    date = models.DateTimeField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    home_goals = models.IntegerField(null=True, blank=True)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')
    away_goals = models.IntegerField(null=True, blank=True)
    score = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
            db_table = 'fixtures'


