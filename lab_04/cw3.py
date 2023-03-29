#Napisz skrypt, który pobiera od użytkownika wartość liczbową, a następnie wyświetla na konsoli 
#zdanie w postaci: "Podaną liczbę można zapisać jako: ...", gdzie zapis będzie w postaci sumy 
#iloczynów liczb dla każdego rzędu. Np. liczba 123: "Podaną liczbę można zapisać jako: 
#100 * 1 + 10 * 2 + 1 * 3". Do pobrania i wypisania wartości użyj odpowiednio instrukcji 
#readline() i write() z modułu sys).

import sys

print("Podaj wartośc liczbową: ")
wartosc = int(sys.stdin.readline())
dlugosc = len(str(wartosc))

print("Podaną liczbę można zapisać jako: ")
for i in str(wartosc):
    sys.stdout.write("1")
    for j in range(dlugosc-1):
        sys.stdout.write("0")
    dlugosc -= 1
    sys.stdout.write(f' * {i}')
    if dlugosc !=0:
        sys.stdout.write(" + ")
        

