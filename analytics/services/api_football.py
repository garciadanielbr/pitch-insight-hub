import requests
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Read .env file

API_KEY = env('API_FOOTBALL_KEY')

class APIFootball:
    BASE_URL = "https://v3.football.api-sports.io/"
    
    def __init__(self, api_key):
        self.headers = {
            "x-rapidapi-key": api_key
        }
    
    def _make_request(self, endpoint, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        print(response.json())
        return response.json()
    
    def get_teams(self, league_id, season):
        return self._make_request("teams", {"league": league_id, "season": season})
    
    def get_players(self, team_id, season):
        return self._make_request("players", {"team": team_id, "season": season})
    
    def get_matches(self, league_id, season):
        return self._make_request("fixtures", {"league": league_id, "season": season})

# Usage
# Get API key from environment variable

# Initialize API client
api = APIFootball(API_KEY)
premier_league_teams = api.get_teams(league_id=39, season=2022)
