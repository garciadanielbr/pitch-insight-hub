from django.db import connection
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Team deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

class FixtureView(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer


class TeamFormGuideView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        last_n_matches = request.query_params.get('last_n_matches', 5)
        try:
            last_n_matches = int(last_n_matches)
        except ValueError:
            return Response({"error": "Invalid last_n_matches parameter"}, status=status.HTTP_400_BAD_REQUEST)

        with connection.cursor() as cursor:
            cursor.execute("SELECT calculate_form_guide(%s, %s)", [team_id, last_n_matches])
            form_guide = cursor.fetchone()[0]

        return Response({
            "team_id": team_id,
            "team_name": team.name,
            "form_guide": form_guide,
            "last_n_matches": last_n_matches
        })
        