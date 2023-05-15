from mod1 import dodawanie
from mod1 import odejmowanie
from mod1 import mnozenie
from mod1 import dzielenie

while True:
    print("Wybierz operację kalkulatora: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, 0 - koniec")
    operacja = int(input("operacja nr: "))
    if operacja == 0:
        print("dziękujemy za skorzystanie z kalkulatora")
        break
    if operacja == 1:
         print("Podaj liczby: ")
         a = int(input())
         b = int(input())
         print(a, "+", b, "=", dodawanie(a,b))
    elif operacja == 2:
         print("Podaj liczby")
         a = int(input())
         b = int(input())
         print(a, "-", b, "=", odejmowanie(a,b))
    elif operacja == 3:
         print("Podaj liczby")
         a = int(input())
         b = int(input())
         print(a, "*", b, "=", mnozenie(a,b))
    elif operacja == 4:
         print("Podaj liczby")
         a = int(input())
         b = int(input())
         print(a, "/", b, "=", dzielenie(a,b))
    else:
        print("proszę wybrać operację z zakresu 0 - 4")





