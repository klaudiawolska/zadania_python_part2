slowo = input("podaj dowolne słowo: ")

palin = (slowo[::-1])
if palin == slowo:
    print("twoje słowo jest palindromem")
else:
    print("twoje słowo nie jest palindomem")