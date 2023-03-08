#Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py 
#i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”, 
#których nie było w przykładach z tego podrozdziału (np. z wyrównaniem do prawej 
#lub lewej strony, ilością pozycji liczby, znakiem, wypełnieniem spacji itp.). 
#Przerób zaprezentowane tam przykłady tak, żeby korzystały z zapisu w postaci f-string.

print(f'{"Przykladowytekst":10.5}!')
print(f'{42:d}')
print(f'{42:f}')
print(f'{3.41592653589793:f}')
print(f'{42:4d}')
print(f'{42:+d}')

data = {'jeden': 'Hura', 'dwa': 'Hura!'}
tekst = '{jeden} {dwa}'.format(**data)
print(f'{tekst}')

