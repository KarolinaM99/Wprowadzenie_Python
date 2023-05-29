import csv
import re 

with open('log.txt', 'r') as file:
    plik = file.read()
  
data = re.compile('\w{3}\s{1}\d{1,}\s{1}\d{2}[:]\d{2}[:]\d{2}')
ip = re.compile('\w{2}[-]\d{2}[-]\d{2}[-]\d{2}[-]\d{3}')
datazapis = re.findall(data, plik)
ipzapis = re.findall(ip, plik)
#Mar 27 13:06:56
datazapis = [d.replace(' ', '-').replace(':', '-') for d in datazapis]

with open('cw2.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(zip(datazapis, ipzapis))
