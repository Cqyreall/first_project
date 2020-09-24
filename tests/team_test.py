import unittest

from models.team import Team
from models.player import Player

class TestTeam(unittest.TestCase):

    def setUp(self):
        team_1 = Team("Barcelona", 27)
        team_2 = Team("Real Madrid", 24)
        self.teams = [team_1, team_2]

        self.player_1 = Player("Hazard", "Real Madrid", "Forward", 12, 8, 0, 0)
        self.player_2 = Player("Rodrygo", "Real Madrid", "Forward", 4, 9, 0, 0)
    
    def test_team_has_name(self):
        team_name = self.teams[1].name
        self.assertEqual("Real Madrid", team_name)
    
    def test_team_has_points(self):
        team_points = self.teams[0].points
        self.assertEqual(27, team_points)
    
    def test_team_has_players(self):
        self.team = Team("Barcelona", 27)
        self.team.add_player(self.player_1)
        self.team.add_player(self.player_2)
        self.assertEqual(2, len(self.team.players))

    


