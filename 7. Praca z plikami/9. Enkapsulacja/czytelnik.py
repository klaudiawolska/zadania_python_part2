class Czytelnik:
    id: int = -1

    def __init__(self,
                 imie : str, nazwisko: str, wiek: int, miasto:str, kod_pocztowy: int, rok_urodzenia: int):
        Czytelnik.id += 1

        self.__id = Czytelnik.id
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wiek = wiek
        self.__miasto = miasto
        self.__kod_pocztowy = kod_pocztowy
        self.__rok_urodzenia = rok_urodzenia
        
    def pobierz_id(self) -> int:
        return self.__id
    def pobierz_imie(self) -> str:
        return self.__imie
    def pobierz_nazwisko(self) -> str:
        return self.__nazwisko
    def pobierz_wiek(self) -> int:
        return self.__wiek
    def pobierz_miasto(self) -> str:
        return self.__miasto
    def pobierz_kod_pocztowy(self) -> int:
        return self.__kod_pocztowy
    def pobierz_rok_urodzenia(self) -> int:
        return self.__rok_urodzenia
    
    