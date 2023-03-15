#Wykorzystaj moduł string i następnie:
#wczytaj ze standardowego wejścia dowolny łańcuch znaków,
#używając formatowania znaków wyświetl ile oraz jaki % znaków (zamienionych na małe litery) 
#z wprowadzonego tekstu pokrywa się z: string.ascii_lowercase, string.digits.

import string 
tekst = input("Podaj dowolny tekst: ")
tekst.lower()
settekst = (set(tekst))

lowercase = set(string.ascii_lowercase)
digits =  set(string.digits) 

pokrywanie_lowercase_procent = len(settekst & lowercase) / len(settekst) * 100
pokrywanie_digits_procent = len(settekst & digits) / len(settekst) * 100

print("Znaki z tego tekstu pokrywają się w {}% ze znakami string.ascii_lowercase\nPokrywa się w nim {} znaków".format(pokrywanie_lowercase_procent, len(settekst & lowercase)))
print("Cyfry z tego tekstu pokrywają się w {}% z cyframi string.digits\nPokrywają się w nim {} cyfry".format(pokrywanie_digits_procent, len(settekst & digits)))