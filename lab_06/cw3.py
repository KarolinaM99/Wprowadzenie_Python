#Napisz funkcję, która będzie zwracała n największych lub najmniejszych wartości (odpowiednia wartość parametru) 
#z listy numerycznej. Lista jest parametrem wejściowym funkcji. W funkcji sprawdzaj czy lista zawiera tylko liczby.

def zad3(lista: list, n, naj=False):
    for i in lista:
        if i != int(i):
            return "Lista nie zawiera tylko liczb"
    return sorted(lista, reverse=naj)[:n]
        
            
            
            
print(zad3([1,2,3,1,4,5,6,7], 3, False))
print(zad3([1,2,3,1,4,5,6,7], 3, True))