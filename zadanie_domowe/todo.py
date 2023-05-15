import json
from os import path


#klasa zadanie i atrybuty obiektu zadanie
class Zadanie:
    id: int = -1

    def __init__(self, tytul: str, opis: str, deadline: int):
        self.__id = Zadanie.id
        self.__tytul = tytul
        self.__opis = opis
        self.__deadline = deadline
    def __str__(self):
        return f"Zadanie ID: {self.Zadanie.id}\nTytul: {self.title}\nDeadline: {self.deadline}"
    def pobierz_opis(self) -> str:
        return self.__opis

#klasa z operacjami wykonywanymi na zadaniach
class Operacje:
    def __init__(self):
        self.zadania = []
        self.wyswietl_zadania()
    
    #metoda do wyswietlania zadań z pliku json
    def wyswietl_zadania(self):
        try:
            dir_path = path.dirname(__file__)
            filename = "plik.json"
            data_path = path.join(dir_path, filename)
            if not path.exists(data_path):
                exit()
            with open(data_path, "r", encoding="utf-8") as plik:
                dane = json.load(plik)
                self.zadania = dane['zadania']
                print(f"Wczytano zadania TO-DO z pliku {filename}")
        except FileNotFoundError:
            print(f"Plik o nazwie: {filename} nie istnieje")
        except json.JSONDecodeError:
            print("Błąd dekodowania pliku JSON")
    
    #metoda do zapisu zadań
    def zapisz_zadania(self):
        dane = {'zadania':self.zadania}
        try:
            dir_path = path.dirname(__file__)
            filename = "plik.json"
            data_path = path.join(dir_path, filename)
            if not path.exists(data_path):
                exit()
            with open(data_path, "r", encoding="utf-8") as plik_zapis:
                plik_zapis.write(dane)
            print(f"Zadanie poprawnie zapisane w pliku {filename}")
        except Exception as e:
            print("Zadania niepoprawnie zapisane")
    
    #metoda do dodawania zadań
    def dodaj_zadanie(self):
        print("Wprowadź informacje o zadaniu, które chcesz dodać")
        Zadanie.id =+ 1
        tytul = input("Tytuł: ")
        opis = input("Opis: ")
        deadline = input("Deadline: ")

        zadanie = Zadanie(Zadanie.id, tytul, opis, deadline)
        self.zadania.append(zadanie)
        print("Dodano nowe zadanie")
    
    #metoda do usuwania zadań
    def usun_zadanie(self):
        zadanie_id = input("Podaj ID zadania do usunięcia: ")
        wyszukane_zadanie = None
        for zadanie in self.zadania:
            if zadanie.Zadanie.id == zadanie_id:
                wyszukane_zadanie = zadanie
                break
        if wyszukane_zadanie:
            self.zadania.remove(wyszukane_zadanie)
            print("Zadanie zostało usunięte")
        else:
            print("Nie znaleziono zadania o podanym ID")

    #metoda do aktualizacji zadań
    def aktualizuj_zadanie(self):
        zadanie_id = input("Podaj ID zadania do usunięcia: ")
        wyszukane_zadanie = None
        for zadanie in self.zadania:
            if zadanie.Zadanie.id == zadanie_id:
                wyszukane_zadanie = zadanie
                break
        if wyszukane_zadanie:
            print("Wprowadź nowe dane o zadaniu, które chcesz zaktualizować")
            tytul = input("Nowy tytuł: ")
            opis = input("Nowy opis: ")
            deadline = input("Nowy deadline: ")

            wyszukane_zadanie.tytul = tytul
            wyszukane_zadanie.opis = opis
            wyszukane_zadanie.deadline = deadline

            print("Zadanie zostało zaktualizowane")
        else:
            print("Nie znaleziono zadania o podanym ID")

    #metoda wyświetlająca listę zadań TO-DO
    def lista_zadan(self):
        if self.zadania:
            for zadanie in self.zadania:
                print(zadanie)
                opis_zadania = input("Czy wyświetlić opis zadania? (t/n)")
                if opis_zadania.lower() == "t":
                    print(zadanie.pobierz_opis())
        else:
            print("Brak zadań na liście")
    
    #metoda do zapisu zadań ręcznie przez uzytkownika
    def zapis_reczny(self):
        print("Ręczne zapisanie zadań do pliku .json")
        print("Aktualne zadania na liście: ")
        self.lista_zadan()
        wybor_zapisu = input("Czy chcesz zapisać aktualne zadania do pliku? (t/n)")
        if wybor.lower() == "t":
            self.zapisz_zadania(filename)
        else:
            print("Zadania nie zostały zapisane do pliku .json")

    