#Napisz funkcję, która przyjmuje listę plików oraz nazwę nowego pliku jako argumenty wejściowe. 
#Funkcja scala zawartość plików w jeden plik wynikowy o podanej wcześniej nazwie.

def scala(lista: list, nazwapliku):
    plik = []
    for i in lista:
        with open(i) as file_reader:
            for linia in file_reader:
                plik.append(linia)
    
    open(nazwapliku, 'w').writelines(plik)
    
scala(['/Volumes/Trenscend/dswp_python/lab_06/zamowienia_polska.csv', '/Volumes/Trenscend/dswp_python/lab_06/zamowienia_niemcy.csv'], nazwapliku= 'zad2.txt')