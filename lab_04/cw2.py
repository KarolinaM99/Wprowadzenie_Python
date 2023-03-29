#Napisz skrypt, który pobiera od użytkownika wartość i:
#sprawdzaj czy podana wartość jest rzutowalna na typ int i float i wyświetl stosowne komunikaty.

wartosc = input("Podaj wartość: ")

try:
    int(wartosc)
    print("Wartość jest rzutowalna na typ int")
except ValueError:
    print("Wartośc nie jest rzutowalna na typ int")
    

try:
    float(wartosc)
    print("Wartość jest rzutowalna na typ float")
except ValueError:
    print("Wartość nie jest rzutowalna na typ float")