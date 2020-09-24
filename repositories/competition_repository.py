from db.run_sql import run_sql

from models.competition import Competition
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

def save(competition):
    sql = "INSERT INTO competitions (team_id, game_id) VALUES (%s, %s) RETURNING *"
    values = [competition.team.id, competition.game.id]
    results = run_sql(sql, values)
    competition.id = results[0]['id']
    return competition

def select_all():
    competitions = []

    sql = "SELECT * FROM competitions"
    results = run_sql(sql)

    for row in results:
        team = team_repository.select(row['team_id'])
        game = game_repository.select(row['game_id'])
        competition = Competition(team, game, row['id'])
        competitions.append(competition)
    return competitions

def delete_all():
    sql = "DELETE * FROM competitions"
    run_sql(sql)






