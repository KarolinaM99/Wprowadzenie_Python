lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

imie = 'Karolina'
nazwisko = 'Maliszewska'

litera1 = nazwisko[3]
litera2 = imie[2]

liczbal1 = lorem.count(litera1)
liczbal2 = lorem.count(litera2)
print("W tekście lorem jest ",liczbal1," liter ",litera1," oraz ",liczbal2," liter ",litera2)