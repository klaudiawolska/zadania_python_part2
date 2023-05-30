import random

liczba = (random.randint(0, 101))

while True:
    zgadnieta = int(input("zgadnięta liczba: "))
    if zgadnieta > liczba:
        print("wylosowana liczba jest mniejsza")
        print("czy grasz jeszcze?")
        odp = input("wpisz 'tak' lub 'nie': ")
        if odp == "tak":
            continue
        elif odp == "nie":
            break
    elif zgadnieta < liczba:
        print("wylosowana liczba jest większa")
        print("czy grasz jeszcze?")
        odp = input("wpisz 'tak' lub 'nie': ")
        if odp == "tak":
            continue
        elif odp == "nie":
            break
    else:
        print("zgadłeś wylosowaną liczbę!")
        break
