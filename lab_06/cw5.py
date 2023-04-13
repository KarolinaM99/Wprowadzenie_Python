#Napisz funkcję:
#parametr wejściowy to lista stringów z nazwiskami
#funkcja zapisuje do dwóch oddzielnych plików o nazwach ‘A-M_nazwiska.txt’ oraz ‘N-Ż_nazwiska.txt’ 
#odpowiednie nazwiska z podanej listy
#Możesz wykorzystać moduł unidecode, który należy uprzednio zainstalować.


def zad4(lista: list):
    am = []
    nz = []
    
    for i in lista:
        if i[0].lower() <= 'm':
            am.append(i)
        else:
            nz.append(i)
    
    with open('/Volumes/Trenscend/dswp_python/lab_06/A-M_nazwiska.txt', 'w') as file:
        file.write('\n'.join(am))
    with open('/Volumes/Trenscend/dswp_python/lab_06/N-Z_nazwiska.txt', 'w') as file2:
        file2.write('\n'.join(nz))


print(zad4(['Maliszewska','Nowak','Michalski','Kowalski']))
        