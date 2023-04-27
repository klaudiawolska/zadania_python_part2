krotka = (10,-3,4,9,12,-6,0)

najmniejsza = krotka[0]
najwieksza = krotka[0]

for i in krotka:
    if najmniejsza > i: 
        najmniejsza = i
    if najwieksza < i:
        najwieksza = i

print ("najmniejsza liczba to:", najmniejsza)
print ("największa liczba to:", najwieksza)