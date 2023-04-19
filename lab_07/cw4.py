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