from os import path

def kombinacjeFunkcja() -> None:
    
    dir_path = path.dirname(__file__)
    imiona = "imiona.txt"
    nazwiska = "nazwiska.txt"
    kombinacje_plik = "plik.txt"
    data_path1 = path.join(dir_path, imiona)
    data_path2 = path.join(dir_path, nazwiska)
    data_path3 = path.join(dir_path, kombinacje_plik)

    if not path.exists(data_path1):
        exit()
    if not path.exists(data_path2):
        exit()

    with open(data_path1, "r", encoding="utf-8") as plik1:
        imiona_odczyt = plik1.readlines()
    with open(data_path2, "r", encoding="utf-8") as plik2:
        nazwiska_odczyt = plik2.readlines()

    for i in range (len(imiona_odczyt)):
        imiona_odczyt[i] = imiona_odczyt[i].strip()

    for i in range (len(nazwiska_odczyt)):
        nazwiska_odczyt[i] = nazwiska_odczyt[i].strip()

    liczba_kombinacji = int(input("Podaj liczbę kombinacji imion i nazwisk: "))

    kombinacje = []

    for imie in imiona_odczyt:
        if(len(kombinacje) == liczba_kombinacji): 
            break
        for nazwisko in nazwiska_odczyt:
            kombinacje.append(imie + " " + nazwisko)
            if(len(kombinacje) == liczba_kombinacji): 
                break

    with open(data_path3,'w',encoding="utf-8") as plik3:
        for kombinacja in kombinacje:
            plik3.write(kombinacja + '\n')

    print("Wygenerowane kombinacje:")
    for kombinacja in kombinacje:
        print(kombinacja)

    print(f'Wygenerowano i zapisano {liczba_kombinacji} kombinacji (dostępne w pliku "plik.txt"')


kombinacjeFunkcja()

