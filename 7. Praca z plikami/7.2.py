from os import path
import random

def kombinacjeFunkcja(imiona, nazwiska, liczba_kombinacji):
    
    with open(data_path1, "r", encoding="utf-8") as plik1:
        imiona_odczyt = plik1.read().splitlines()
    with open(data_path2, "r", encoding="utf-8") as plik2:
        nazwiska_odczyt = plik2.read().splitlines()

    kombinacje = set()

    while len(kombinacje) < liczba_kombinacji:
            imie = random.choice(imiona_odczyt)
            nazwisko = random.choice(nazwiska_odczyt)
            kombinacja = f'{imie} {nazwisko}'
            kombinacje.add(kombinacja)

    with open('plik.txt','w') as plik3:
       plik3.write(kombinacja + '\n')
    
    print("Wygenerowane kombinacje:")
    for kombinacja in kombinacje:
        print(kombinacja)


dir_path = path.dirname(__file__)
imiona = "imiona.txt"
nazwiska = "nazwiska.txt"
data_path1 = path.join(dir_path, imiona)
data_path2 = path.join(dir_path, nazwiska)
if not path.exists(data_path1):
    exit()
if not path.exists(data_path2):
    exit()


liczba_kombinacji = int(input("Podaj liczbę kombinacji imion i nazwisk: "))

kombinacjeFunkcja(imiona, nazwiska, liczba_kombinacji)
print(f'Wygenerowano i zapisano {liczba_kombinacji} kombinacji (dostępne w pliku "plik.txt"')

