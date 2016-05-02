import fisher_yates

class game:
    def __init__(self, p1, p2):
        self._player1 = p1[0]
        self._deck1 = p1[0]
        
        self._player2 = p2[0]
        self._deck2 = p2[0]
        
        self._hand1 = []
        self._hand2 = []
    
    
    def start(self):
        shuffle(self._deck1)
        shuffle(self._deck2)
        
                