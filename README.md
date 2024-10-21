# Pitch Insight Hub

## Football Analytics Platform

Pitch Insight Hub is a Django-based football analytics platform that demonstrates advanced data processing and analysis capabilities using PostgreSQL. This project showcases skills in Django, PostgreSQL, Docker, API integration, and complex SQL queries.

### Key Features

- Integration with API-Football for comprehensive football data
- Advanced SQL queries for in-depth football analytics
- Docker-based setup for easy deployment and development
- Django admin interface for easy data management

## Technologies Used

- Django
- PostgreSQL
- Docker
- API-Football integration

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/garciadanielbr/pitch-insight-hub.git
   cd pitch-insight-hub
   ```

2. Copy the `.env.example` file to `.env` and update the values:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file to include your specific settings, including database credentials and API keys.

3. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

4. Once the containers are running, open a new terminal and run the initial data population script:
   ```
   docker exec -it web python manage.py populate_initial_data
   ```

   This will populate the database with initial leagues and seasons data.

### Usage

1. Access the Django admin interface at `http://localhost:8000/admin/` to manage leagues and seasons and `http://localhost:8000/api/` for the API.

2. Create a Superuser
   To access the Django admin interface, you need to create a superuser. Run the following command in your terminal:
   ```
   docker exec -it web python manage.py createsuperuser
   ```
   Follow the prompst to set a username, email and password.

3. Before fetching data, set the `fetch_required` flag to True for the seasons you want to update. You can do this either through the Django admin interface or directly in the database.

4. Use the provided management commands to fetch data from API-Football:
   ```
   docker exec -it web python manage.py fetch_teams
   docker exec -it web python manage.py fetch_fixtures
   docker exec -it web python manage.py fetch_players
   ```
   Note: These commands will only fetch data for seasons where `fetch_required` is True. After successful data fetching, the flag is automatically set to False.

5. Explore the API endpoints for analytics:
   - Form Guide: `GET /api/teams/<team_id>/form-guide/`

## Advanced Queries

This project demonstrates the use of advanced SQL queries for football analytics. For example, the Form Guide calculation uses a complex SQL function to analyze team performance based on recent matches, considering factors like match recency and opponent strength.

## Future Plans

- Implement more advanced analytics and data visualizations
- Develop a user-friendly front-end interface
- Expand data collection from API-Football to cover more aspects of football analytics

## Contributing

This project is primarily for portfolio demonstration purposes. However, if you have suggestions or find bugs, please open an issue in the GitHub repository.

## License

This project is open-source and available under the MIT License.