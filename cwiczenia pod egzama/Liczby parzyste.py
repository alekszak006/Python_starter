parzyste = 0
nieparzyste = 0
suma = 0

for i in range (10):
    liczba = int(input("podaj liczbe"))
    suma += liczba

    if liczba % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(parzyste)
print(nieparzyste)
print(suma)