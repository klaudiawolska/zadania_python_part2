from os import path
import string 
dir_path = path.dirname(__file__)
filename = "text.txt"
data_path = path.join(dir_path, filename)

if not path.exists(data_path):
    exit()

with open(data_path, "r", encoding="utf-8") as plik:
    text = plik.read()

liczba_slow = len(text.split())
print("Liczba słów w tekście: ", liczba_slow)

litera_koncowa = {}
for slowo in text.split():
    slowo = slowo.strip(string.punctuation)  # Usunięcie znaków interpunkcyjnych z słowa
    litera = slowo[-1].lower()  
    if litera.isalpha():  
        if litera in litera_koncowa:
            litera_koncowa[litera] += 1
        else:
            litera_koncowa[litera] = 1

print("Liczba słów w tekście:", liczba_slow)
print("Statystyki końcowych liter słów:")
for litera, liczba in litera_koncowa.items():
    print(f"{litera.upper()}: {liczba}")






