from django.db import transaction
from ..models import League, Season, Team, SeasonTeam, Fixture
from .api_football import api_client

def populate_initial_data():
    leagues_data = [
        {'name': 'Premier League', 'country': 'England', 'type': 'League', 'id': 39},
        {'name': 'Serie A', 'country': 'Italy', 'type': 'League', 'id': 135},
        {'name': 'La Liga', 'country': 'Spain', 'type': 'League', 'id': 140},
    ]
    
    seasons_data = [
        {'league_id': 39, 'year': 2022},
        {'league_id': 135, 'year': 2022},
        {'league_id': 140, 'year': 2022},
    ]
    
    with transaction.atomic():
        for league_info in leagues_data:
            League.objects.get_or_create(
                id=league_info['id'],
                defaults={
                    'name': league_info['name'],
                    'country': league_info['country'],
                    'type': league_info['type']
                }
            )
        
        for season_info in seasons_data:
            Season.objects.get_or_create(
                league_id=season_info['league_id'],
                year=season_info['year']
            )

@transaction.atomic
def fetch_and_store_teams():
    seasons_to_fetch = Season.objects.filter(fetch_required=True)
    
    if not seasons_to_fetch.exists():
        return 'No seasons available to fetch data.'

    new_teams_count = 0  # Counter for new teams added

    for season in seasons_to_fetch:
        teams_data = api_client.get_teams(season.league.id, season.year)
        
        for team_data in teams_data['response']:
            team, created = Team.objects.update_or_create(
                id=team_data['team']['id'],
                defaults={
                    'name': team_data['team']['name'],
                    'country': team_data['team']['country']
                }
            )

            if created:  # Check if the team was newly created
                new_teams_count += 1
            
            SeasonTeam.objects.get_or_create(
                season=season,
                team=team
            )
        
        season.fetch_required = False
        season.save()

    if new_teams_count > 0:
        return f'Successfully fetched and stored {new_teams_count} teams data.'
    else:
        return 'Data fetched successfully but no new teams were added.'

@transaction.atomic
def fetch_and_store_fixtures():
    seasons_to_fetch = Season.objects.filter(fetch_required=True)

    if not seasons_to_fetch.exists():
        return 'No seasons available to fetch data.'

    new_fixtures_count = 0  # Counter for new fixtures added 

    for season in seasons_to_fetch:
        fixtures_data = api_client.get_fixtures(season.league.id, season.year)
        
        for fixture_data in fixtures_data['response']:
            fixture, created = Fixture.objects.update_or_create(
                id=fixture_data['fixture']['id'],
                defaults={
                    'season': season,
                    'round': fixture_data['league']['round'],
                    'date': fixture_data['fixture']['date'],
                    'home_team_id': fixture_data['teams']['home']['id'],
                    'home_goals': fixture_data['goals']['home'],
                    'away_team_id': fixture_data['teams']['away']['id'],
                    'away_goals': fixture_data['goals']['away'],
                    'score': fixture_data['score']
                }
            )

            if created:  # Check if fixture was newly created
                new_fixtures_count += 1
        
        season.fetch_required = False
        season.save()  

    if new_fixtures_count > 0:
        return f'Successfully fetched and stored {new_fixtures_count} fixtures data.'
    else:
        return 'Data fetched successfully but no new fixtures were added.'      