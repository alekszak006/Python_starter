from io import StringIO

n = int(input("wprowadz jedna zmienna"))

for i in range(n):
    for j in range(1, i):
        print("*",end=" ")
    print(" ")

