'''03 prednaska 8.10.2024

- platnost promennych
    - Sccope = oblast platnosti promennych
    - promene se rozdeluji na globals and locals
'''

# globalni prostor
import math


C = 3
a = 1
VERBOSITY = 3  # takhle delat globalni promenne/konstanta
# python nema metodu ktera zabranuje prepisovani konstant


# lokalni prostor
def my_function(x):
    a = 9 + C  # a je tady lokalni a neprepise globalni a - proto to nepojmenovavat stejne
    return x + a


def main():
    C = 99
    a = 2
    b = my_function(a)
    print(a, b, C)


print(a)

# lokalni prostor
if __name__ == '__main__':
    a = 2
    b = my_function(a)
    print(a, b, C)
    a = 0.3
    b = 3 * 0.1
    print(a == b)  # false
    print(math.isclose(a, b))  # true
    main()
# math.isclose(a, b)
