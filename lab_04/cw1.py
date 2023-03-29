#Pobieraj z klawiatury wartość w postaci liczby całkowitej, a następnie wyświetl 
#ją w postaci liczby binarnej, ósemkowej i szesnastkowej.

liczba = int(input("Podaj liczbę całkowitą: "))

print(f"Twoja liczba w postaci binarnej: {bin(liczba)}")
print(f"Twoja liczba w postaci ósemkowej: {oct(liczba)}")
print(f"Twoje liczba w postaci szesnastkowej: {hex(liczba)}")