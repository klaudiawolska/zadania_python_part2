def dodawanie(a: float,b: float) -> float:
    """wykonuje dodawanie"""
    return a + b

#błędny typ dla zmiennej b > string, gdy type hinting > float
''' def dodawanie(a: float,b: string) -> float:
    """wykonuje dodawanie"""
    return a + b '''

def odejmowanie(a: float,b:float) -> float:
    """wykonuje odejmowanie"""
    return a - b

def mnozenie(a:float,b:float) -> float:
    """wykonuje mnozenie"""
    return a*b

def dzielenie(a:float,b:float) -> float:
    """wykonuje dzielenie"""
    return a / b

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





