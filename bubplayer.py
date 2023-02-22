class Player:
    def __init__(self, p_id):
        self.lives = 3
        self.player_id = p_id

    def sendLives(self):
        return self.lives

    def sendID(self):
        return self.player_id

    