from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import team_repository
from models.team import Team

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/new")
def new_team():
    teams = team_repository.select_all()
    return render_template("teams/new.html", teams=teams)

@teams_blueprint.route("/teams", methods=['POST'])
def create_team():
    name = request.form['name']
    points = request.form['points']
    new_team = Team(name, points)
    team_repository.save(new_team)
    return redirect('/teams')

@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect ('/teams')

@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    teams = team_repository.select_all()
    return render_template ("teams/edit.html", team=team, teams=teams)

@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update(id):
    name = request.form['name']
    points = request.form['points']
    updated_team = Team(name, points, id)
    team_repository.update(updated_team)
    return redirect("/teams")

@teams_blueprint.route("/teams/delete", methods=['POST'])
def delete_league():
    team_repository.delete_all()
    return redirect("/teams")










