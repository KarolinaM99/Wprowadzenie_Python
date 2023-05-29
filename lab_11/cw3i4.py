
import pickle


class imieinazwisko:
    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def wys(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

imieinaz = imieinazwisko("Karolina","Maliszewska")

with open('person.txt', 'wb') as file:
    pickle.dump(imieinaz, file)


with open('person.txt', 'rb') as file:
    loaded_person = pickle.load(file)
    
loaded_person.wys()

osoba1 = imieinazwisko("Karolina", "Maliszewska")
osoba2 = imieinazwisko("Jan", "Kowalski")
osoba3 = imieinazwisko("Anna", "Nowak")

lista_obiektow = [osoba1, osoba2, osoba3]

with open('person.txt', 'wb') as file:
    pickle.dump(lista_obiektow, file)

with open('persons.txt', 'rb') as file:
    loaded_list = pickle.load(file)

for obiekt in loaded_list:
    obiekt.wys()