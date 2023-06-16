import json

#klasa zadanie i atrybuty obiektu zadanie
class Zadania:

    id: int = 0

    def __init__(self, tytul: str, opis: str, deadline: str):
        Zadania.id += 1
        self.__id = Zadania.id
        self.__tytul = tytul
        self.__opis = opis
        self.__deadline = deadline
        
    #metoda do wyświetlania opisu
    def pobierz_opis(self) -> str:
        return self.__opis
    
    #metoda do wyświetlania id
    def pobierz_id(self) -> int:
        return self.__id
    
    #metoda do wyświetlania informacji o zadaniu
    def pobierz_zadanie(self) -> str:
        return f"Zadanie ID: {self.__id}\nTytul: {self.__tytul}\nDeadline: {self.__deadline}"

    #metoda do dodawania zadań
    def dodaj_zadanie() -> object:
        tytul = input("Tytuł: ")
        opis = input("Opis: ")
        deadline = input("Deadline: ")

        zadanie = Zadania(tytul,opis,deadline)
        return zadanie 
    
    def zmien_tytul(self,nowy_tytul:str) -> None:
        self.__tytul = nowy_tytul

    def zmien_opis(self,nowy_opis:str) -> None:
        self.__opis = nowy_opis

    def zmien_deadline(self,nowy_deadline:str) -> None:
        self.__deadline = nowy_deadline

#metoda do usuwania zadań
def usun_zadanie(lista, id_zadania) -> None:
    i = 0
    szukane_id = False
    for zadanie in lista:
        if zadanie.pobierz_id() == id_zadania:
            del lista[i]
            szukane_id = True
            print("Zadanie zostało usunięte")
            break
        else:
            szukane_id = False
            i += 1
            print("Nie znaleziono zadania o podanym ID")

#metoda do aktualizacji zadań
def aktualizuj_zadanie(lista, id_zadania) -> None:
    szukane_id = False
    for zadanie in lista:
        if zadanie.pobierz_id() == id_zadania:
            print("Wprowadź nowe dane o zadaniu, które chcesz zaktualizować")
            nowy_tytul = input("Nowy tytuł: ")
            nowy_opis = input("Nowy opis: ")
            nowy_deadline = input("Nowy deadline: ")
            zadanie.zmien_tytul(nowy_tytul)
            zadanie.zmien_opis(nowy_opis)
            zadanie.zmien_deadline(nowy_deadline)
            print("Zadanie zostało zaktualizowane")
            szukane_id = True
            break
        else:
            szukane_id = False
            print("Nie znaleziono zadania o podanym ID")
        

#metoda do wyświetlania zadania o wskazanym id
def wyswietl_zadanie_id(lista, id_zadania) -> None:
    szukane_id = False
    for zadanie in lista:
        if zadanie.pobierz_id() == id_zadania:
            print(zadanie.pobierz_zadanie())
            opis_zadania = input("Czy wyświetlić opis zadania? (t/n)")
            if opis_zadania.lower() == "t":
                print(zadanie.pobierz_opis())
            szukane_id = True
            break
        else:
            print("Nie znaleziono zadania o podanym ID")

#encoder do wyświetlania danych z pliku o fromacie json 
class ZadanieEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Zadania):
            return obj.__dict__
        return super().default(obj)

#decoder json
class ListDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if isinstance(dct, dict) and not dct:  
            return []  
        if '_Zadania__id' in dct and '_Zadania__tytul' in dct and '_Zadania__opis' in dct and '_Zadania__deadline' in dct:
            return Zadania(dct['_Zadania__tytul'], dct['_Zadania__opis'], dct['_Zadania__deadline'])
        return dct

#metoda do pobierania zadań z pliku json
def wyswietl_zadania(filename):
    try:
        with open(filename, 'r') as plik:
            dane = json.load(plik, cls=ListDecoder)
            return dane
    except FileNotFoundError:
        print(f"Plik o nazwie: {filename} nie istnieje")
    except json.JSONDecodeError:
        print("Błąd dekodowania pliku JSON")

#metoda do wyświetlania całej listy zadań TO-DO
def lista_zadan(lista) -> None:
    if len(lista) != 0:
        for zadanie in lista:
            print(zadanie.pobierz_zadanie())
            opis_zadania = input("Czy wyświetlić opis zadania? (t/n)")
            if opis_zadania.lower() == "t":
                print(zadanie.pobierz_opis())
    else:
        print("Brak zadań na liście")