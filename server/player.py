class player:
    self._maxdecks = 9
    
    def __init__(self, nickname, password):
        self._login = nickname
        self._password = password
        
    
    def create(self):
        self._rank = 25
        self._stars = 0
        
        self._decks = []
       
    
    def load(self):
        path = "./" + self.login + "/decks"