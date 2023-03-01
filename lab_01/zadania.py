#Przestudiuj dokumentację opisującą typ int oraz float i napisz kod, 
#w którym stworzysz po dwa obiekty typu int i float tak z użyciem 
#różnych wartośxi dla konstruktorów tych typów 
#(np. z inną podstawą niż domyślne 10 dla typu int).

int_1 = 20
int_2 = int(0b1100)

float_1 = 5.4
float_2 = float(0b11001)
print("Zadanie 1 - Typ int")
print(int_1, int_2) 
print("\nZadanie 1 - Typ float ")
print(float_1, float_2)


#Napisz kod, w którym wykorzystasz poniższe metody dla typów:
#int.bit_count()
#float.is_integer()

print("\nZadanie 2 - metoda int.bit_count()")
int_3 = 2001
print(bin(int_3))
print(int_3.bit_count())

print("\nZadanie 2 - metoda float.is_integer()")
float_3 = 50.33
float_4 = 20.0
print(float_3)
print(float_3.is_integer())
print(float_4)
print(float_4.is_integer())

#Przygotuj 4 przykłady kodu, który będzie wykorzystywał operatory bitowe.
print("\nZadanie 3")
bit_1 = 0b1010
bit_2 = 0b1011
print(bit_1 << 3)
print(bit_1 >> 2)
print(~bit_1)
print(bit_1 ^ bit_2)
