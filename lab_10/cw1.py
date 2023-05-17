import os

def foldery(sciezka):
    for s in sciezka:
        if not os.path.exists(s):
            os.makedirs(s)
            
            
sciezka = ['lab_10/chciałem','lab_10/chciałem/być','lab_10/chciałem/być/marynarzem']
foldery(sciezka)