#Napisz funkcję, która wyświetla podany tekst odwracając kolejność liter w wyrazach. Np. „Ala ma kota” 
#wyświetli „alA am atok”

def zad6(tekst):
    slowa = tekst.split()
    odwroc = [i[::-1] for i in slowa]
    return ' '.join(odwroc)

print(zad6('Ala ma kota'))