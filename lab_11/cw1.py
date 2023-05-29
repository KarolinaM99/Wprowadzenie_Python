import re


with open('string.txt', 'r') as file:
    plik = file.read()


liczby = re.findall(r'\d+', plik)
liczby3 = re.findall(r'\d{3,}', plik)
ipv4 = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', plik)
wielkie = re.findall(r'\b[A-Z]\w*\b', plik)
wyrazy4 = re.findall(r'^(?:\w+\s+){3,}\w+$', plik)
url = re.findall(r'\b(?:https?|ftp)://\S+\b', plik)



print("Wszystkie liczby:", liczby)
print("Wszystkie liczby co najmniej 3-cyfrowe:", liczby3)
print("Wszystkie adresy IPv4:", ipv4)
print("Wszystkie wyrazy rozpoczynające się od wielkiej litery:", wielkie)
print("Wszystkie linie z co najmniej 4 wyrazami:", wyrazy4)
print("Wszystkie adresy url: ", url)
