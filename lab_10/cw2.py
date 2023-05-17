import csv
import os
import string


def foldery(path: string) -> None:
    with open('lab_10/zad2.csv', 'w', newline='') as csvfile:
        zapis = csv.writer(csvfile,delimiter=";")
        kol = ""
        for root, _, files in os.walk(path):
            for file in files:
                with open(root+"/"+file , 'r') as f:
                    if kol == "":
                        kol = f.readline().removesuffix("\n").split(",")
                        zapis.writerow(kol)
                    else:
                        f.readline()
                    for line in f:
                        zapis.writerow(line.removesuffix("\n").split(","))
                        
foldery("lab_10/data_for_lab_10")