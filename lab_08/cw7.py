from collections import deque
import random
import time

from cw6 import create_kolo_fortuny


def spinit(fortune: deque, wygrana: int):
    fortune.rotate(random.randint(0, len(fortune)))

    print(f"Aktualny stan koła: {fortune}")
    if fortune[0] != wygrana:
        time.sleep(1)
        spinit(fortune, wygrana)
       
fortune = create_kolo_fortuny(9,2,3,4,5,6,7,8,1)
wygrana = fortune[0] #albo random.choice(fortune)

fortune.rotate(1)
spinit(fortune, wygrana)
print("Wygrałeś")
    