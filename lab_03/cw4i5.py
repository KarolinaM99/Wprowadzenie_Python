#Stwórz słownik gdzie kluczami będą numery miesięcy (rozpoczynając od 1),
#a wartościami nazwy polskich miesięcy.

slownikpl = {
    1 : 'Styczeń',
    2 : 'Luty',
    3 : 'Marzec',
    4 : 'Kwiecień',
    5 : 'Maj',
    6 : 'Czerwiec',
    7 : 'Lipiec',
    8 : 'Spierpień',
    9 : 'Wrzesień',
    10 : 'Październik',
    11 : 'Listopad',
    12 : 'Grudzień'
}

#Stwórz podobny słownik jak w zadaniu 1, ale z angielskimi nazwami miesięcy. 
#Połącz teraz słowniki tak, żeby przykładowo dla kwietnia, 
#dostać się poprzez wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez months['en'][4].

slowniken = {
   1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December' 
}

polaczone = {'Polskie': slownikpl, 'Angielskie': slowniken}
print(polaczone['Polskie'][4])
print(polaczone['Angielskie'][4])
