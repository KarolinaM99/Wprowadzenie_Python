#Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, 
#aby pierwsze 5 liczb zostało w oryginalnej liście a pozostałe 5 znalazło się w nowej liście.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista[5:]
del lista[5:]
print("Lista1: ",lista,"\nLista2: ",lista2)

#Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. 
#Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.

lista = [0] + lista + lista2
print("Listy po połączeniu i dodaniu wartości 0 na początku: ",lista)