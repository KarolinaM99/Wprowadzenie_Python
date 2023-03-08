#Napisz fragment kodu, który wczyta trzy zmienne z klawiatury:
#linię danych rozdzielonych jakimś separatorem (spacja, średnik, itd.)
#separator źródłowy
#separator docelowy
#Następnie zaimplementuj z użyciem metod split oraz join podzielenie wejścia 
#pierwszym separatorem, połączenie i wypisanie danych połączonych drugim separatorem.

zdanie = input("Wpisz zdanie z jakimś separatorem (spacja, średnik, itd.) ")
sep1 = input("Podaj separator jakiego użyłeś ")
sep2 = input("Podaj separator na jaki zamienić ")

split = zdanie.split(sep1)
zdanie = sep2.join(split)
print(zdanie)