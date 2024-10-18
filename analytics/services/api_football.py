from tenacity import retry, stop_after_attempt, wait_exponential
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
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def _make_request(self, endpoint, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        #print(response.json())
        return response.json()
    
    def get_teams(self, league_id, season):
        return self._make_request("teams", {"league": league_id, "season": season})
    
    def get_players(self, team_id, season):
        return self._make_request("players", {"team": team_id, "season": season})
    
    def get_matches(self, league_id, season):
        return self._make_request("fixtures", {"league": league_id, "season": season})
    
    def get_fixtures(self, league_id, season):
        return self._make_request("fixtures", {"league": league_id, "season": season})


# Usage
# Initialize API client
api_client = APIFootball(API_KEY)
'''
premier_league_teams = api.get_teams(league_id=39, season=2022)

if 'response' in premier_league_teams:
    print(f"Successfully retrieved {len(premier_league_teams['response'])} teams.")
    # Print the first team's name as an example
    if premier_league_teams['response']:
        print(f"First team: {premier_league_teams['response'][0]['team']['name']}")
else:
    print("Failed to retrieve teams.")
    print("Response:", premier_league_teams)


# Test function to get teams
def test_get_teams():
    # Premier League ID is 39
    teams = api.get_teams(league_id=39, season=2023)
    
    if 'response' in teams:
        print(f"Successfully retrieved {len(teams['response'])} teams.")
        # Print the first team's name as an example
        if teams['response']:
            print(f"First team: {teams['response'][0]['team']['name']}")
    else:
        print("Failed to retrieve teams.")
        print("Response:", teams)

# Run the test
if __name__ == "__main__":
    test_get_teams()
''' 