#Napisz wyrażenie generujące, które będzie zwracało krotkę dwuwartościową postaci: 
#('Ala', [65, 108, 97]), ('ma', [109, 97]), ('kota.', [107, 111, 116, 97, 46]) dla 
#przykładowego zdania Ala ma kota. Dla każdego wyrazu z tekstu przekazanego jako argument 
#wejściowy tego wyrażenia zwraca ten wyraz oraz listę wartości int odpowiadającą kodowi 
#tego znaku z tablicy znaków (zobacz wbudowane ord(), chr()).

zdanie = "Ala ma kota."
result = [(word, [ord(char) for char in word]) for word in zdanie.split()]
print(result)