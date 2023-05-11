class Czytelnik:
    id: int = -1

    def __init__(self,
                 imie : str, nazwisko: str, wiek: int, miasto:str, kod_pocztowy: int, rok_urodzenia: int):
        Czytelnik.id += 1

        self.id = Czytelnik.id
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy
        self.rok_urodzenia = rok_urodzenia
        