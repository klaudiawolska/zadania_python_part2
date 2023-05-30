lista = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]

litera = input("wprowadź literę, na którą ma zaczynać się słowo: ")

for i in lista:
    if i[0:1] == litera:
        print(i, end=" ")
    