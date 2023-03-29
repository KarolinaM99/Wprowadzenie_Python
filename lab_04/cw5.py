#Napisz skrypt, który pobiera z klawiatury zdanie, a na konsoli wyświetla 
#wyrazy z tego zdania posortowane według ich długości rosnąco.

zdanie = input("Podaj zdanie: ")
wyrazy = zdanie.split(" ")

print(sorted(wyrazy, key=len))