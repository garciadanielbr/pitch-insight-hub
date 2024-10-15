from django.db import models
from django.db.models import Avg, Sum

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