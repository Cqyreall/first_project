from db.run_sql import run_sql

from models.team import Team

def save(team):
    sql = "INSERT INTO teams (name, points) VALUES (%s, %s) RETURNING *"
    values = [team.name, team.points]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['points'], row['id'])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['points'], result['id'])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET (name, points) = (%s, %s) WHERE id = %s"
    values = [team.name, team.points, team.id]
    run_sql(sql, values)


# def select_games_to_be_played(id):
#     games = []

#     sql = "SELECT games.* FROM games INNER JOIN games"
