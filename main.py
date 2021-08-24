import deviceDB
import sys
import modelsDB
import json

#Poczatek - generowanie bazy lub nie

print("Generowanie bazy...")
try:
    file = open("netbox_devices.txt", "x") #x nie doda pliku, gdy juz istnieje
    file.write("name,device_role,tenant,manufacturer,device_type,status,position,face,rack,site")
    file.close()
except:
    print("Plik istnieje. Wygenerowac nowy? (y/n)")
    newFileBoolean = input()
    if newFileBoolean == "y":
        file = open("netbox_devices.txt", "w") #w nadpisze dokument
        file.write("name,device_role,tenant,manufacturer,device_type,status,position,face,rack,site")
        file.close()
    else: pass

#Koniec generowania bazy


print("Wprowadz nazwe urzadzenia:")
dname = input()
if dname== "po" or dname == "pm" or dname == "pp":
    dmodel = "PP"
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
print("Podaj nazwe 'rack' (szafy) lub nacisnij enter aby pozostawic pole puste do pozniejszego wypelnienia: ")
drack = input()
print("Podaj nazwe 'site' (wezla sieciowego) lub nacisnij enter aby pozostawic pole puste do pozniejszego wypelnienia: ")
dsite = input()
deviceDB.device_database(dname,dmodel,duList,drack,dsite)
