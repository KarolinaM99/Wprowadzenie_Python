#Wczytaj plik zamowienia.csv i dokonaj w nim kilku przekształceń:
#pozbądź się znaku z (właściwie zł) z kolumny Utarg
#zamień separator wartości dziesiętnej w tej samej kolumnie na '.'
#pozbądź się spacji jako separatora tysięcy w kolumnie Utarg
#zamień format daty w pliku na RRRR-MM-DD (wykorzystaj moduł datetime)
#Podziel plik na dwie części i zapisz je tak, aby dane dla każdego kraju (Polska, Niemcy) 
#znajdowały się w oddzielnych plikach o nazwach zamowienia_polska.csv i zamowienia_niemcy.csv.

import csv
import datetime

polska= []
niemcy = []

with open('/Volumes/Trenscend/dswp_python/lab_06/zamowienia.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for wiersz in reader:
        wiersz['Utarg'] = wiersz['Utarg'].replace('z', '').replace(',', '.').replace(' ', '')
        wiersz['Data zamowienia'] = datetime.datetime.strptime(wiersz['Data zamowienia'], '%d.%m.%Y').strftime('%Y-%m-%d')
        if wiersz['Kraj'] == 'Polska':
            polska.append([wiersz['Sprzedawca'], wiersz['Data zamowienia'], wiersz['idZamowienia'], wiersz['Utarg']])
        elif wiersz['Kraj'] == 'Niemcy':
            niemcy.append([wiersz['Sprzedawca'], wiersz['Data zamowienia'], wiersz['idZamowienia'], wiersz['Utarg']])


with open('/Volumes/Trenscend/dswp_python/lab_06/zamowienia_polska.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])
    writer.writerows(polska)

with open('/Volumes/Trenscend/dswp_python/lab_06/zamowienia_niemcy.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])
    writer.writerows(niemcy)      