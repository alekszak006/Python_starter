class Pojazd:
    def __init__(self,liczba_kol,silnik):
        self.liczba_kol=liczba_kol
        self.silnik=silnik
class Samochod(Pojazd):
    def __init__(self,liczba_kol,silnik):
        super().__init__(liczba_kol,silnik)