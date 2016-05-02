# This class for card in leshastone

class card:
    def __init__(self, path):
        self._path = path
        self.load()

        
    def down_cost(self, cnt=0):
        self._nowcost = max(0, self._nowcost - cnt)

        
    def up_cost(self, cnt=0):
        self._nowcost += cnt
    
    
    def silence(self):
        self._effects.clear()
        self._nowhealth = min(self._nowhealth, self._health)
        self._nowdamage = self.damage

        
    def give_event(self, event):
        return