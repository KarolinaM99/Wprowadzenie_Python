wyrazy = input("Podaj listę róznych wyrazów: ").split(" ")
posortowane = sorted(wyrazy, key=lambda w: len(w), reverse=True)
print(posortowane)