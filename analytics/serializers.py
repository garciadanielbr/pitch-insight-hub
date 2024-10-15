from rest_framework import serializers
from .models import Player, Match, PlayerPerformance

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PlayerPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPerformance
        fields = '__all__'