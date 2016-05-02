import random

def shuffle(array):
    for i in range(len(array)):
        pos = random.randint(0, i)
        array[i], array[pos] = array[pos], array[i]