#Napisz funkcję, która:
#przyjmuje z klawiatury n, będące liczbą całkowitą
# wykonuje n rzutów kostką k6 i zwraca listę krotek wartości postaci 
#('oczka: 6', 'rzutów: i') itd., gdzie zmienna i jest ilością rzutów dla tej liczby oczek. 
#Dodaj odpowiedni type hinting.

from typing import List, Tuple
import random

def rzut_kostka(n: int) -> List[Tuple[str, int]]:
    results = []
    for i in range(n):
        results2 = random.randint(1, 6)
        results.append(('oczka: {}'.format(results2), 'rzutów: {}'.format(i+1)))
    return results


print(rzut_kostka(3))