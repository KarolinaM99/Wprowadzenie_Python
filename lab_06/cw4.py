#Mając listę mieszana = [1, 2.3, ‘Zbyszek’, 5, ‘Marian’, 3.0] napisz funkcję, która zapisze wartości dla każdego 
#typu do słownika gdzie pod kluczem równym nazwie typu zmiennej (int, float, str, itp.) wartością będzie lista 
#elementów z listy 'mieszana' danego typu. Przykład: {'int': [1,5], 'str': ['Zbyszek','Marian']} itd.

def zad4(lista: list ):
    slownik = {}
    for i in lista:
        typee = type(i) 
        if typee not in slownik:
            slownik[typee] = []
        slownik[typee].append(i)
    return slownik

mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
print(zad4(mieszana))