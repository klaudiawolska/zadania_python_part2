import random

while True:
    liczba = (random.randint(0, 101))
    proby = 0

    while True:
        zgadnieta = int(input("zgadnięta liczba: "))
        proby += 1

        if zgadnieta > liczba:
            print("wylosowana liczba jest mniejsza")
        elif zgadnieta < liczba:
            print("wylosowana liczba jest większa")
        else:
            print("zgadłeś wylosowaną liczbę!")
            print("zgadłeś po:" ,proby , "próbach")
            print("czy grasz jeszcze?")
            odp = input("wpisz 'tak' lub 'nie': ")
            if odp == "tak":
                break
            elif odp == "nie":
                exit()
            

