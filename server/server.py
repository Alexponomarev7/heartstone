import socket
import threading
import collections
from game import game

def load():
    # loading server
    return


def start():
    # starting server
    return


def finish():
    # finishing server
    return


def making_games():
    # creating games between players
    global find_players
    
    while True:
        if len(find_players) < 2:
            continue
        
        player1 = find_players.popleft()
        player2 = find_players.popleft()    
        
        make_log(player1, player2)
        threading.Thread(target=game(player1, player2).start).start()
        

if __name__ == '__main__':
    start()
    
    find_players = collections.deque()
    threading.Thread(target=making_games).start()
    
    
    
    finish()