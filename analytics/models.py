from django.db import models
from django.db.models import Avg, Sum

class League(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'leagues'

class Season(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    year = models.IntegerField()
    fetch_required = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
            db_table = 'seasons'
class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
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



class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=100)

    def average_goals_per_match(self):
        return self.playerperformance_set.aggregate(Avg('goals'))['goals__avg'] or 0

    def total_assists(self):
        return self.playerperformance_set.aggregate(Sum('assists'))['assists__sum'] or 0
    
    def __str__(self):
        return self.name + ' (' + self.team + ')'

class Match(models.Model):
    date = models.DateField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    def total_goals(self):
        return self.home_score + self.away_score
    
    def __str__(self):
        return self.home_team + ' ' + str(self.home_score) + 'x' + ' ' + str(self.away_score) + ' ' + self.away_team + ' (' + str(self.date) + ')'

class PlayerPerformance(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)