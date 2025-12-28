

class ArrayOperations:
    def __init__(self):
        self.array = [0] * 10

    def read_array(self):
        print("Podaj 10 liczb całkowitych:")
        for i in range(10):
            self.array[i] = int(input(f"Liczba {i + 1}: "))

    def __find_max_index(self, start_index):
        max_index = start_index
        for i in range(start_index + 1, len(self.array)):
            if self.array[i] > self.array[max_index]:
                max_index = i
        return max_index

    def sort_descending(self):
        for i in range(len(self.array)):
            max_index = self.__find_max_index(i)
            self.array[i], self.array[max_index] = self.array[max_index], self.array[i]

    def display_array(self):
        print("Tablica po sortowaniu malejącym:")
        for value in self.array:
            print(value, end=" ")
        print()


if __name__ == "__main__":
    array_operations = ArrayOperations()
    array_operations.read_array()
    array_operations.sort_descending()
    array_operations.display_array()


