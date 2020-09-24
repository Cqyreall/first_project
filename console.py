import pdb
from models.player import Player
from models.competition import Competition
from models.game import Game
from models.team import Team
from models.user import User

import repositories.team_repository as team_repository
import repositories.game_repository as game_repository
import repositories.competition_repository as competition_repository

# user_1 = User("Cyril Ishabiyi")
team_1 = Team("Barcelona", 27)
team_repository.save(team_1)

team_2 = Team("Real Madrid", 24)
team_repository.save(team_2)

team_3 = Team("Chelsea", 30)
team_repository.save(team_3)

team_4 = Team("Manchester City", 2)
team_repository.save(team_4)

team_5 = Team("Manchester United", 6)
team_repository.save(team_5)


game_1= Game("El Clasico", 3, 0)
game_repository.save(game_1)

game_2 = Game("Manchester Derby", 4, 0)
game_repository.save(game_2)




competition_1 = Competition(team_1, game_1)
competition_repository.save(competition_1)

competition_2 = Competition(team_2, game_1)
competition_repository.save(competition_2)

competition3 = Competition(team_4, game_2)
competition_repository.save(competition3)

competition4 = Competition(team_5, game_2)
competition_repository.save(competition4)

games = game_repository.teams(game_1)

print(games[0].__dict__)


# team_repository.select_all()


# team = team_repository.select(2)

# team_repository.delete(3)

# print(team.__dict__)

pdb.set_trace()