import mod1

while True:
     print("Wybierz operację kalkulatora: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, 0 - koniec")
     operacja = int(input("operacja nr: "))
     if operacja == 0:
          print("dziękujemy za skorzystanie z kalkulatora")
          break
     try:
          a = float(input("Podaj a:"))
          b = float(input("Podaj b:"))
          
          if operacja == 1:
               print(a, "+", b, "=", mod1.dodawanie(a,b))
          elif operacja == 2:
               print(a, "-", b, "=", mod1.odejmowanie(a,b))
          elif operacja == 3:
               print(a, "*", b, "=", mod1.mnozenie(a,b))
          elif operacja == 4:
               print(a, "/", b, "=", mod1.dzielenie(a,b))
          else:
               print("proszę wybrać operację z zakresu 0 - 4")
               
     except ValueError:
          print("Błędne dane, podaj liczby")
     except ZeroDivisionError:
          print("Nie mona dzielić przez zero")
     finally:
          print("Operacja zakończona :)")
        




