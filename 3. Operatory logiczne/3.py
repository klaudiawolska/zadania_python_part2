wiek = int(input("podaj swój wiek: "))

kategoria = True if input("czy masz prawo jazdy kat. A2? (t/n): ") in ("t","ta","tak","T") else False
czasA2 = 0
if kategoria:
    czasA2 = int(input("jak długo masz prawo jazdy kategorii A2? Podaj ilość lat: "))

if wiek > 20 and czasA2 > 2:
    print("mozesz przystąpić do egzaminu")
elif wiek >= 24:
    print("mozesz przystąpić do egzaminu")
else:
    print("nie mozesz przystąpić do egzaminu")

