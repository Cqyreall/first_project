import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        player_1 = Player("Messi", "Barcelona", "Forward", 50, 22, 0, 0)
        player_2 = Player("Ronaldo", "Juventus", "Forward", 30, 20, 0, 0)
        self.players = [player_1, player_2]
    
    def test_player_has_name(self):
        player_name = self.players[0].name
        self.assertEqual("Messi", player_name)
    
    def test_player_has_team(self):
        player_team = self.players[1].team
        self.assertEqual("Juventus", player_team)
    
    def test_player_has_goals(self):
        player_goals = self.players[0].goals
        self.assertEqual(50, player_goals)
    
    def test_player_has_yellow_cards(self):
        player_yellow_cards = self.players[1].yellow_cards
        self.assertEqual(0, player_yellow_cards)
        