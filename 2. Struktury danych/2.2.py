slowo = input("podaj dowolne słowo: ")

for i in slowo:
    palin = (slowo[::-1])
    if palin == slowo:
        print("twoje słowo jest palindromem")
        break
    else:
        print("twoje słowo nie jest palindomem")
        break