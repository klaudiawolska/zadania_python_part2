from czytelnik import Czytelnik

czytelnik_1 = Czytelnik(
    imie = "Jan",
    nazwisko = "Kowalski",
    wiek = 22,
    miasto = "Szczecin",
    kod_pocztowy = 71123,
    rok_urodzenia = 2001
)

czytelnik_2 = Czytelnik(
    imie = "Kasia",
    nazwisko = "Kwiatek",
    wiek = 23,
    miasto = "Szczecin",
    kod_pocztowy = 71113,
    rok_urodzenia = 2000
)
czytelnik_3 = Czytelnik(
    imie = "Ada",
    nazwisko = "Kotek",
    wiek = 20,
    miasto = "Szczecin",
    kod_pocztowy = 71123,
    rok_urodzenia = 2003
)

czytelnik_1.__id = 10
print(czytelnik_1.pobierz_id())
czytelnik_1.__imie = "Dawid"
print(czytelnik_1.pobierz_imie())
print(czytelnik_1.pobierz_nazwisko())