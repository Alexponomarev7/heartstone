# gamedeck

class deck:
    _maxsize = 30
    
    def __init__(self):
        self._cards = []
        self._manacurve = [0] * 8
    

    def full(self):
        return len(self._cards) == 30
        
    
    def add_card(self, card):
        if self.full():
            return
        
        self._manacurve[card._manacost] += 1
        self._cards.append(card)