from db.run_sql import run_sql

from models.game import Game
from models.team import Team

def save(game):
    sql = "INSERT INTO games (name, home_team_goals, away_team_goals) VALUES (%s, %s, %s) RETURNING *"
    values = [game.name, game.home_team_goals, game.away_team_goals]
    results = run_sql(sql,values)
    id = results[0]['id']
    game.id = id
    return game

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        game = Game(row['name'], row['home_team_goals'], row['away_team_goals'], row['id'])
        games.append(game)
    return games

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        game = Game(result['name'], result['home_team_goals'], result['away_team_goals'], result['id'])
    return game



def delete_game(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(game):
    sql = "UPDATE games SET (name, home_team_goals, away_team_goals) = (%s, %s, %s) WHERE id = %s"
    values = [game.name, game.home_team_goals, game.away_team_goals, game.id]
    run_sql(sql, values)

def teams(game):
    teams = []

    sql = "SELECT teams.* FROM teams INNER JOIN competitions on competitions.team_id = teams.id WHERE game_id = %s"
    values = [game.id]
    results = run_sql(sql, values)
    for row in results:
        team = Team(row['name'], row['points'], row['id'])
        teams.append(team)
    return teams

