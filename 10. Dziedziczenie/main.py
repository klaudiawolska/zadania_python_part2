from klasa import Kwadrat, Prostokat, Trojkat, Kolo
import math 

kwadrat = Kwadrat(3)
print("Pole kwadratu: ", kwadrat.pole())
print("Obwód kwadratu: ", kwadrat.obwod())

prostokat = Prostokat(2,5)
print("Pole prostokątu: ", prostokat.pole())
print("Obwód prostokątu: ", prostokat.obwod())

trojkat = Trojkat(3,4,5)
print("Pole trójkątu: ", trojkat.pole())
print("Obwód trójkątu: ", trojkat.obwod())

kolo = Kolo(5)
print("Pole koła: ", kolo.pole())
print("Obwód koła: ", kolo.obwod())

