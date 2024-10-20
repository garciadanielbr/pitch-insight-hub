def get_form_guide_function_sql():
       return """
        CREATE OR REPLACE FUNCTION calculate_form_guide(team_id INT, last_n_matches INT)
        RETURNS FLOAT AS $$
        DECLARE
            form_guide FLOAT := 0;
            max_points FLOAT := 0;
            match_points FLOAT;
            recency_weight FLOAT;
            opponent_strength FLOAT;
            opponent_weight FLOAT;
        BEGIN
            -- Calculate max_points for normalization
            SELECT SUM(POWER(1.1, generate_series))
            INTO max_points
            FROM generate_series(0, last_n_matches - 1);

            -- Calculate form guide
            WITH recent_matches AS (
                SELECT
                    f.id,
                    f.date,
                    f.home_team_id = team_id AS is_home,
                    CASE
                        WHEN f.home_team_id = team_id THEN f.home_goals
                        ELSE f.away_goals
                    END AS team_score,
                    CASE
                        WHEN f.home_team_id = team_id THEN f.away_goals
                        ELSE f.home_goals
                    END AS opponent_score,
                    CASE
                        WHEN f.home_team_id = team_id THEN f.away_team_id
                        ELSE f.home_team_id
                    END AS opponent_id,
                    ROW_NUMBER() OVER (ORDER BY f.date DESC) AS match_number
                FROM
                    fixtures f
                WHERE
                    f.home_team_id = team_id OR f.away_team_id = team_id
                ORDER BY
                    f.date DESC
                LIMIT last_n_matches
            ),
            opponent_strengths AS (
                SELECT
                    t.id AS team_id,
                    (SUM(CASE WHEN f.home_team_id = t.id THEN f.home_goals ELSE f.away_goals END)::FLOAT / COUNT(DISTINCT f.id)) AS avg_goals_scored
                FROM
                    teams t
                    JOIN fixtures f ON f.home_team_id = t.id OR f.away_team_id = t.id
                GROUP BY
                    t.id
            )
            SELECT
                SUM(
                    CASE
                        WHEN rm.team_score > rm.opponent_score THEN 3
                        WHEN rm.team_score = rm.opponent_score THEN 1
                        ELSE 0
                    END * POWER(1.1, rm.match_number - 1) * (os.avg_goals_scored / 2)
                ) / max_points
            INTO form_guide
            FROM
                recent_matches rm
                JOIN opponent_strengths os ON os.team_id = rm.opponent_id;

            RETURN form_guide;
        END;
        $$ LANGUAGE plpgsql;
       """