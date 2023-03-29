#Napisz funkcję, która przyjmuje nieokreśloną liczbę wartości z kluczem. 
#Funkcja przyjmuje argumenty w postaci: klucz to nazwa drużyny a wartość to
#ilość punktów, które drużyna zdobyła. Funkcja zlicza, ile jest wszystkich 
#punktów razem i zwraca tę wartość.

def sumapunktow(**druzyny):
    punkty = 0
    for i in druzyny.values():
        punkty += i
    return punkty

print(sumapunktow(Druzyna1=23, Druzyna2=12, Druzyna3=4, Druzyna4=12))