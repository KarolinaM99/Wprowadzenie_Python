#Wykorzystaj moduł this i korzystając z umieszczonego tam słownika kodującego 
#(sprawdź dostępne zmienne modułu this) napisz skrypt, który będzie kodował 
#tym słownikiem wpisywane zdanie (przechwytuj z klawiatury). 
#Wypisuj na konsoli zakodowane zdanie.

import this

zdanie = input("Podaj zdanie: ")
zakodowane = ""

for i in zdanie:
    if i in this.d:
        zakodowane = zakodowane + this.d[i]
    else:
        zakodowane = zakodowane + i

print("Twoje zdanie zostało zakodowane: " + zakodowane)