from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import game_repository
from models.game import Game

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", games=games)

@games_blueprint.route("/games/<id>")
def fixtures(id):
    game = game_repository.select(id)
    teams = game_repository.teams(game)
    return render_template("games/show.html", game=game, teams=teams)

