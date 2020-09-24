import unittest

from models.game import Game
from models.team import Team
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        player_1 = Player("Messi", "Barcelona", "Forward", 50, 22, 0, 0)
        player_2 = Player("Ronaldo", "Barcelona", "Forward", 30, 20, 0, 0)
        player_3 = Player("Greizman", "Barcelona", "Forward", 15, 10, 0, 1)

        player_4 = Player("Hazard", "Real Madrid", "Forward", 50, 22, 0, 0)
        player_5 = Player("Kroos", "Real Madrid", "Midfielder", 30, 20, 0, 0)
        player_6 = Player("Benzema", "Real Madrid", "Forward", 15, 10, 0, 1)

        team_1 = Team("Barcelona", 27)
        team_2 = Team("Real Madrid", 24)

        team_1.add_player(player_1)
        team_1.add_player(player_2)
        team_1.add_player(player_3)

        team_2.add_player(player_4)
        team_2.add_player(player_5)
        team_2.add_player(player_6)

        self.game = Game("El Clasico", 3, 0)

    
    def test_game_has_location(self):
        self.assertEqual("El Clasico", self.game.name)
    
    def test_game_has_goals(self):
        self.assertEqual(3, self.game.home_team_goals)
    
   



