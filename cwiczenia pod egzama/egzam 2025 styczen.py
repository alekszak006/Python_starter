import random

class TablicaLiczb:
    def __init__(self, rozmiar):
        self.__rozmiar = rozmiar
        self.__tablica = []

        for i in range(self.__rozmiar):
            self.__tablica.append(random.randint(1, 1000))

    def read_array(self):
        for i in range (self.__rozmiar):
            print(i , ":" , self.__tablica[i])

    def szukaj(self, wartosc):
        for i in range (self.__rozmiar):
            if self.__tablica[i] == wartosc:
                return i
        return -1
    def wypisz_nieparzyste(self):
        licznik = 0
        for i in range (self.__rozmiar):
            if self.__tablica[i] %2 != 0:
                licznik += 1
                print(self.__tablica[i])
        print("Liczba liczb nieparzystych:",licznik)

    def licz_arytmetyczna(self):
        suma = 0
        for i in range (self.__rozmiar):
            suma += self.__tablica[i]

        return suma / self.__rozmiar

if __name__ == "__main__":
    t = TablicaLiczb(25)
    t.read_array()
    indeks = t.szukaj(114)
    print("znaleziono na indeksie:", indeks)
    print("Liczby nieparzyste")
    print(t.wypisz_nieparzyste())
    print("Srednia wszystkich elementow")
    print(t.licz_arytmetyczna())
