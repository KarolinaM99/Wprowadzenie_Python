import array
import datetime
import random


# zapisanie tablicy do pliku oraz jej wczytanie
start1 = datetime.datetime.now()

tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])

with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)
    
stop1 = datetime.datetime.now()
print("Czas operacji zapisu danych z tablicy  - ",stop1-start1)

# wczytujemy ponownie dane do tablicy floatów
start2 = datetime.datetime.now()

tab_of_floats_loaded = array('f')
file_arr  = open('floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()

stop2 = datetime.datetime.now()
print("Czas wczytania danych do tablicy - ",stop2-start2)


# i analogiczna operacja dla listy
start3 = datetime.datetime.now()

list_of_floats = [random.random() for _ in range(1_000_000)]
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))

stop3 =datetime.datetime.now()
print("Czas zapisu danych z listy - ",stop3-start3)

start4 = datetime.datetime.now()
with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
stop4 = datetime.datetime.now()
print("Czas wczytania danych do listy - ",stop4-start4)
