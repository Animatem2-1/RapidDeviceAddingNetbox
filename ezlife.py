import  deviceDB
import  sys

print("Witaj Panie! Pustynia czeka na Ciebie.")
print("Aby wygenerowac fundament potrzebny do dodawania sprzetu wpisz 'basic', w innym wypadku wpisz 'nara'.")
begin = input()
if begin == "basic":
    try:
        file = open("netbox.txt", "x") #x nie doda pliku, gdy juz istnieje
        file.write("name,device_role,tenant,manufacturer,device_type,status,site,rack,position,face")
        file.close()
        print("Building completed!")
    except:
        print("Plik już istnieje.")
        sys.exit()
elif begin == "nara":
    print("Przejdzmy do wrzucania!")
else:
    print("Jestes glupi czy nie umiesz czytac po polsku?")
    print("basic czy nara?")
    begin2 = input()
    if begin2 == "nara":
        print("Nie jestes taki glupi na jakiego wygladasz.")
        print("Przejdzmy do wrzucania!")
    else:
        print("Ehhh...")
        sys.exit()

print("Wprowadz nazwe urzadzenia:")
dname = input()
print("Wprowadz skrot modelu urzadzenia:")
dmodel = input()
print("Wprowadz U urzadzenia:")
du = input()
print("Czy chcesz wprowadzic dodatkowe opcje? (Wpisz 'y' jesli tak.)")
ddecision = input()
print("Potwierdz wybor.")
ddecision = input()
if ddecision == "y":
    print("Ilosc dodawanych urzadzen (wieksza niz 0):")
    dno = input()
    while int(dno) <= 0:
        print("Wieksza niz 0!")
        dno = input()
    print("Kierunek dodawania(up/down):")
    ddirection = input()
    while ddirection != "up" and ddirection != "down":
        print("Wybierz Up lub down!")
        ddirection = input()
else:
    pass
deviceDB.device_database(dname,dmodel,du)
