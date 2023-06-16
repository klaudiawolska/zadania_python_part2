import todo_lista 
from todo_lista import Zadania
import json
import os 

try:
    if os.path.exists('plik.json'):
        with open('plik.json', 'r') as plik:
            try:
                dane = json.load(plik)
            except:
                json.dump({}, plik)
        lista = todo_lista.wyswietl_zadania('plik.json')
    else:
        with open('plik.json', 'w') as plik:
            json.dump({}, plik)
        lista = todo_lista.wyswietl_zadania('plik.json')
except:
    print("Błąd listy TO-DO")
    exit()
    
print("Zadania na liście TO-DO: ")
if len(lista) != 0:
    for zadanie in lista:
        print(zadanie.pobierz_zadanie())
else:
    print("Brak zadań na liście TO-DO :)")

#menu programu
while True:
    print("\n PROGRAM \n")
    print("\n -- TO DO LIST -- \n")
    print("\n MENU \n")
    print("1. Dodaj nowe zadanie")
    print("2. Wyświetl zadania")
    print("3. Usuń zadanie")
    print("4. Aktualizuj zadanie")
    print("5. Zapisz ręcznie zadania do pliku")
    print("6. Wyświetl zadanie")
    print("0 - Wyjście z programu")

    wybor_menu = input("Wybierz operację: ")

    if wybor_menu == "1":
        zadanie = Zadania.dodaj_zadanie()
        lista.append(zadanie)

    elif wybor_menu == "2":
        todo_lista.lista_zadan(lista)

    elif wybor_menu == "3":
        try:
            id_zadania = int(input("Podaj ID zadania, które chcesz wyświetlić: "))
            todo_lista.usun_zadanie(lista, id_zadania)
        except:
            print("Nie ma zadania o takim ID")

    elif wybor_menu == "4":
        try:
            id_zadania = int(input("Podaj ID zadania, które chcesz wyświetlić: "))
            todo_lista.aktualizuj_zadanie(lista, id_zadania)
        except:
            print("Nie ma zadania o takim ID")

    elif wybor_menu == "5":
        with open('plik.json','w') as plik:
            json.dump(lista,plik, cls=todo_lista.ZadanieEncoder)
       
    elif wybor_menu == "6":
        try:
            id_zadania = int(input("Podaj ID zadania, które chcesz wyświetlić: "))
            todo_lista.wyswietl_zadanie_id(lista, id_zadania)
        except:
            print("Nie ma zadania o takim ID")

    elif wybor_menu == "0":
        with open('plik.json','w') as plik:
            json.dump(lista, plik, cls=todo_lista.ZadanieEncoder)
       
        print("Dziękujemy za skorzystanie z programu TO-DO LIST")
        exit()
    else:
        print("Nie ma takiej opcji w menu, wybierz spośród 0-6")

