import mod1

while True:
     print("Wybierz operację kalkulatora: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, 0 - koniec")     
     
     try:
          operacja = int(input("operacja nr: "))

          if operacja == 0:
               print("dziękujemy za skorzystanie z kalkulatora")
               break
          elif operacja == 1:
               a = float(input("Podaj a:"))
               b = float(input("Podaj b:"))
               print(a, "+", b, "=", mod1.dodawanie(a,b))
          elif operacja == 2:
               a = float(input("Podaj a:"))
               b = float(input("Podaj b:"))
               print(a, "-", b, "=", mod1.odejmowanie(a,b))
          elif operacja == 3:
               a = float(input("Podaj a:"))
               b = float(input("Podaj b:"))
               print(a, "*", b, "=", mod1.mnozenie(a,b))
          elif operacja == 4:
               a = float(input("Podaj a:"))
               b = float(input("Podaj b:"))
               print(a, "/", b, "=", mod1.dzielenie(a,b))
          else:
               print("proszę wybrać operację z zakresu 0 - 4")
               
     except ValueError:
          print("Błędne dane, podaj liczby")
     except ZeroDivisionError:
          print("Nie mozna dzielić przez zero")
     except Exception as exc:
          print("Błąd: ", str(e))
     finally:
          print("Operacja zakończona :)")
        




