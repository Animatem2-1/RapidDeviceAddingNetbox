import deviceDB
import sys
import modelsDB
import json

#Poczatek - generowanie bazy lub nie
print("Witaj Panie! Pustynia czeka na Ciebie.")
print("Aby wygenerowac fundament potrzebny do dodawania sprzetu wpisz 'baza' lub pomin wciskajac enter.")
begin = input()
if begin == "baza":
    try:
        file = open("netbox.txt", "x") #x nie doda pliku, gdy juz istnieje
        file.write("name,device_role,tenant,manufacturer,device_type,status,rack,position,face,site")
        file.close()
        print("Building completed!")
    except:
        print("Plik już istnieje.")
        sys.exit()
elif begin == "":
    print("Przejdzmy do wrzucania!")
else:
    print("Jestes glupi czy nie umiesz czytac po polsku?")
    print("baza czy pomijasz?")
    begin2 = input()
    if begin2 == "":
        print("Nie jestes taki glupi na jakiego wygladasz.")
        print("Przejdzmy do wrzucania!")
    else:
        print("Ehhh...")
        sys.exit()

#Koniec generowania bazy


print("Wprowadz nazwe urzadzenia:")
dname = input()
if dname== "po" or dname == "pm" or dname == "pp":
    dmodel = "panel"
else:
    print("Wprowadz skrot modelu urzadzenia lub wpisz help, aby wyswietlic pomoc:")
    dmodel = input()
    if dmodel == "help":
        for key in modelsDB.models:
            print(key, ' = ', modelsDB.models[key])
        print("Wprowadz skrot:")
        dmodel = input()
    else: pass
print("Wprowadz U urzadzenia, jesli chcesz dodac to urzadzenie na wielu U przedziel ich numery spacjami:")
du = input()
duList = du.split()
deviceDB.device_database(dname,dmodel,duList)
