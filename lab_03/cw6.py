#Wykorzystując ciąg tekstowy 'Marianna' oraz metodę fromkeys() dla słowników stwórz słownik, 
#który będzie zawierał jako klucze unikalne litery w/w imienia a jako wartość każdy 
#klucz będzie miał przypisaną wartość 1. Poprawne wyjście: {'M': 1, 'a': 1, 'r': 1, 'i': 1, 'n': 1}

tekst = "Marianna"
slownik = dict.fromkeys(tekst, 1)
print(slownik)