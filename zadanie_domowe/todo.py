import json
from os import path


#klasa zadanie i atrybuty obiektu zadanie
class Zadanie:

    id: int = 0

    def __init__(self, id, tytul: str, opis: str, deadline: str):
        Zadanie.id += 1
        self.id = Zadanie.id
        self.tytul = tytul
        self.opis = opis
        self.deadline = deadline
    def __str__(self):
        return f"Zadanie ID: {self.id}\nTytul: {self.tytul}\nDeadline: {self.deadline}"
    def pobierz_opis(self) -> str:
        return self.opis

#
class ZadanieEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Zadanie):
            return {
                'id': obj.id,
                'tytul': obj.tytul,
                'opis': obj.opis,
                'deadline': obj.deadline
            }
        return super().default(obj)

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
                zadania_json = dane.get('zadania', [])  #pobranie listy zadań z pliku json
                self.zadania = [Zadanie(**zadanie) for zadanie in zadania_json]  
                print(f"Wczytano zadania TO-DO z pliku {filename}: ")
                for zadanie in zadania_json: #pętla to odczytania zadań z pliku i wyświetlenia na konsoli
                    zadanie_z_pliku = Zadanie(**zadanie) #tworzenie obiektu zadanie dla kadego elementu
                    print(zadanie_z_pliku)
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
            if not path.isfile(data_path):
                exit()
            with open(data_path, "w", encoding="utf-8") as plik_zapis:
                json.dump(dane, plik_zapis, cls=ZadanieEncoder, ensure_ascii=False, indent=4)
            print(f"Zadanie poprawnie zapisane w pliku {filename}")
        except Exception as e:
            print(f"Zadania niepoprawnie zapisane z powodu błędu: {e}")
    
    #metoda do dodawania zadań
    def dodaj_zadanie(self):
        print("Wprowadź informacje o zadaniu, które chcesz dodać")
        tytul = input("Tytuł: ")
        opis = input("Opis: ")
        deadline = input("Deadline: ")

        zadanie = Zadanie(Zadanie.id, tytul, opis, deadline)
        self.zadania.append(zadanie)
        print("Dodano nowe zadanie")
    
    #metoda do usuwania zadań
    def usun_zadanie(self):
        zadanie_id = int(input("Podaj ID zadania do usunięcia: "))
        wyszukane_zadanie = None
        for zadanie in self.zadania:
            if Zadanie.id == zadanie_id:
                wyszukane_zadanie = zadanie
                break
        if wyszukane_zadanie:
            self.zadania.remove(wyszukane_zadanie) #usunięcie wybranego zadania
            print("Zadanie zostało usunięte")
            self.zapisz_zadania() #zapisanie zmienionej listy zadań
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
        if wybor_zapisu.lower() == "t":
            self.zapisz_zadania()
        else:
            print("Zadania nie zostały zapisane do pliku .json")

    