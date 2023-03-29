#Wykorzystując poprzedni przykład z listingu 11 zdefiniuj funkcję, która będzie przyjmowała 
#obiekty typu str jako wejście (dowolną liczbę), a będzie zwracała listę tych łańcuchów 
#posortowaną alfabetycznie.

def sortuj(* text: str) -> list():
    if len(text) == 0:
        return list()
    else:
        return sorted([ x for x in text ])
    
print(sortuj('c','d','az','es','pp','er'))