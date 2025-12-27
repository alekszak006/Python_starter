def Euklides(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

try:
    a=int(input())
    b=int(input())
    if a>0 and b>0:
        wynik = Euklides(a,b)
        print(wynik)
    else:
        print("Podaj liczby dodatnie")
except ValueError:
    print("Podaj liczbe calkowita")


