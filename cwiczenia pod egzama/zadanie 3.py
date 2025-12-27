import math
import math as m

a,b,c = map(int,input("podaj wspolczynniki").split())

if a==0:
    print("to nie jest f kwadratowa")
else:
    delta = b*b - 4*c*a
    if delta>0:
        x=(-b+math.sqrt(delta))/2*a
        y=(-b-math.sqrt(delta))/2*a
        print(x,y)
    elif delta < 0:
        print("brak rozw")
    elif delta == 0:
        x=-b/2
        print(x)
