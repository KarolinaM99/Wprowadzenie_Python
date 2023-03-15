#Napisz skrypt, który pobierze dowolny tekst ze standardowego wejścia poprzez funckję input(). 
#Następnie wyświetl ciąg unikalnych znaków z wczytanego zdania, zapisanych alfabetycznie małymi literami.

tekst = input("Podaj dowolny tekst: ")
tekst.lower()
uni = sorted(set(tekst))
print("Unikalne znaki w twoim tekscie: ", uni)