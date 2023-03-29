#Wygeneruj macierz (lista dwupoziomowa) losowych wartości (sprawdź pakiet random) 4x4 
#i wykorzystując Python comprehension zdefiniuj listę, która będzie zawierała tylko 
#elementy znajdujące się na głównej przekątnej.

import random 

macierz = [[random.randint(0, 9) for j in range(4)] for i in range(4)]
print(macierz)

przekatna = [macierz[i][i] for i in range(4)]
print(przekatna)