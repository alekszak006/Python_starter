import random

class ArrayOperations:
    def __init__(self, size):
        """
               **********************************************
               nazwa metody: __init__
               opis metody: Konstruktor klasy. Przyjmuje rozmiar tablicy
                            i wypełnia ją pseudolosowymi liczbami całkowitymi.
               parametry:
               size: int - rozmiar tablicy, liczba elementów w tablicy
               zwracany typ i opis: brak
               autor: Aleks Żak
               **********************************************
               """
        self.size = size
        self.array = [random.randint(1, 1000) for _ in range(size)]

    def display_all(self):
        for index, value in enumerate(self.array):
            print(f"{index}: {value}")

    def search(self, value):
        """
               **********************************************
               nazwa metody: search
               opis metody: Wyszukuje pierwsze wystąpienie wartości w tablicy.
                            Zwraca indeks, lub -1 jeśli element nie został znaleziony.
               parametry:
               value: int - wartość, którą szukamy w tablicy
               zwracany typ i opis: int - indeks znalezionego elementu lub -1, jeśli nie znaleziono
               autor: Aleks Żak
               **********************************************
               """
        try:
            return self.array.index(value)
        except ValueError:
            return -1

    def display_odd(self):
        """
               **********************************************
               nazwa metody: display_odd
               opis metody: Wyszukuje i wyświetla wszystkie liczby nieparzyste z tablicy
                            oraz zwraca ich ilość.
               parametry: brak
               zwracany typ i opis: int - liczba liczb nieparzystych w tablicy
               autor: Aleks Żak
               **********************************************
               """
        odd_numbers = [num for num in self.array if num % 2 != 0]
        print("Nieparzyste liczby:", odd_numbers)
        return len(odd_numbers)

    def calculate_average(self):
        """
               **********************************************
               nazwa metody: calculate_average
               opis metody: Oblicza średnią arytmetyczną wszystkich wartości w tablicy.
               parametry: brak
               zwracany typ i opis: float - średnia arytmetyczna wartości w tablicy
               autor: Aleks Żak
               **********************************************
               """
        return sum(self.array) / len(self.array)




if __name__ == "__main__":
    array_size = 25
    array_ops = ArrayOperations(array_size)

    print("Wszystkie elementy tablicy:")
    array_ops.display_all()

    search_value = 500
    index = array_ops.search(search_value)
    if index != -1:
        print(f"Wartość {search_value} znajduje się na indeksie {index}.")
    else:
        print(f"Wartość {search_value} nie została znaleziona.")

    odd_count = array_ops.display_odd()
    print(f"Ilość liczb nieparzystych: {odd_count}")

    average = array_ops.calculate_average()
    print(f"Średnia arytmetyczna wartości w tablicy: {average:.2f}")
