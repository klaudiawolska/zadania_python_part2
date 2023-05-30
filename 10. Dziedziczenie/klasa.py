from abc import ABC, abstractmethod
import math 

class Figura(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def pole(self):
        pass
    @abstractmethod
    def obwod(self):
        pass

class Kwadrat(Figura):
    def __init__(self, bok_kwadratu):
        super().__init__()
        self.__bok_kwadratu = bok_kwadratu
    def pole(self):
        return self.__bok_kwadratu * self.__bok_kwadratu
    def obwod(self):
        return 4 * self.__bok_kwadratu

class Prostokat(Figura):
    def __init__(self,bok_a,bok_b):
        super().__init__()
        self.__bok_a = bok_a
        self.__bok_b = bok_b
    def pole(self):
        return self.__bok_a * self.__bok_b
    def obwod(self):
        return (2 * self.__bok_a) + (2 * self.__bok_b)

class Trojkat(Figura):
    def __init__(self,bok_a,bok_b,bok_c):
        super().__init__()
        self.__bok_a = bok_a
        self.__bok_b = bok_b
        self.__bok_c = bok_c
    def pole(self):
        pole_trojkata = (self.__bok_a + self.__bok_b  + self.__bok_c) / 2
        return math.sqrt(pole_trojkata * (pole_trojkata - self.__bok_a) * (pole_trojkata-self.__bok_b) * (pole_trojkata-self.__bok_c))
    def obwod(self):
        return self.__bok_a + self.__bok_b + self.__bok_c
    
class Kolo(Figura):
    def __init__(self, promien):
        super().__init__()       
        self.__promien = promien
    def pole(self):
        return math.pi * (self.__promien**2)
    def obwod(self):
        return 2 * math.pi * (self.__promien)
    
