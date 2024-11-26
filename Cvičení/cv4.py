# 6 3 2 4
# 5 1 6 3
# 8 9 1 0
import random


class My_class:

    def print_data(array):
        a = 0
        b = 0
        for i in range(len(array)):
            if a < max(array[i]):
                a = max(array[i])
            if b > min(array[i]):
                b = min(array[i])

        len_max = len(str(a))
        len_min = len(str(b))
        print(a, b)
        print(len_max, len_min)

        for i in range(len(array)):
            for s in range(len(array[i])):
                print(f"{array[i][s]}", end=" ")
            print('')

    def generate_data(n_rows, n_cols):
        array = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        for i in range(n_rows):
            for s in range(n_cols):
                array[i][s] = random.randint(0, 1)
        return (array)


if __name__ == "__main__":
    data = [[6, 3, 2, 4,], [5000, 1, 6, 3], [-8000, 9, 1, 0]]
    My_class.print_data(data)
    print('')
    new = My_class.generate_data(2, 20)
    My_class.print_data(new)

    cislo = 1
    print(f'Tohle je cislo: {cislo}')

    number = 7
    print(f"{number:5}")  # Right-align with spaces (total width 5)
