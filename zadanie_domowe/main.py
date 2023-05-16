from todo import Zadanie, Operacje

#wyświetlanie zadań na liście przy uruchomieniu programu
operacje = Operacje()
operacje.wyswietl_zadania()

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
    print("0 - Wyjście z programu")

    wybor_menu = input("Wybierz operację: ")

    if wybor_menu == "1":
        operacje.dodaj_zadanie()
    elif wybor_menu == "2":
        operacje.wyswietl_zadania()
    elif wybor_menu == "3":
        operacje.usun_zadanie()
    elif wybor_menu == "4":
        operacje.aktualizuj_zadanie()
    elif wybor_menu == "5":
        operacje.zapis_reczny()
    elif wybor_menu == "0":
        operacje.zapisz_zadania()
        print("Dziękujemy za skorzystanie z programu TO-DO LIST")
        break
    else:
        print("Nie ma takiej opcji w menu, wybierz spośród 0-5")

