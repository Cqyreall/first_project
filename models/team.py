class Team:

    def __init__(self, name, points, id=None):
        self.name = name
        self.points = points
        self.id = id
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)