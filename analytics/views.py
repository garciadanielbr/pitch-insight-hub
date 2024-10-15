from rest_framework import viewsets, views
from rest_framework.response import Response
from django.db.models import Avg, Sum, Q
from .models import Player, Match, PlayerPerformance
from .serializers import PlayerSerializer, MatchSerializer, PlayerPerformanceSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class PlayerPerformanceViewSet(viewsets.ModelViewSet):
    queryset = PlayerPerformance.objects.all()
    serializer_class = PlayerPerformanceSerializer

class TopScorersView(views.APIView):
    def get(self, request):
        top_scorers = Player.objects.annotate(total_goals=Sum('playerperformance__goals')).order_by('-total_goals')[:10]
        return Response([{"name": player.name, "total_goals": player.total_goals} for player in top_scorers])

class TeamPerformanceView(views.APIView):
    def get(self, request):
        teams = set(Player.objects.values_list('team', flat=True))
        team_stats = []
        for team in teams:
            matches_played = Match.objects.filter(Q(home_team=team) | Q(away_team=team)).count()
            goals_scored = Match.objects.aggregate(
                total_goals=Sum('home_score', filter=Q(home_team=team)) + 
                            Sum('away_score', filter=Q(away_team=team))
            )['total_goals'] or 0
            goals_conceded = Match.objects.aggregate(
                total_goals=Sum('away_score', filter=Q(home_team=team)) + 
                            Sum('home_score', filter=Q(away_team=team))
            )['total_goals'] or 0
            team_stats.append({
                "team": team,
                "matches_played": matches_played,
                "goals_scored": goals_scored,
                "goals_conceded": goals_conceded
            })
        return Response(team_stats)