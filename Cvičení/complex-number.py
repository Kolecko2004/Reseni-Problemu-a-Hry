class ComplexNumber:
    '''Metoda objektu, vol8 se jenom s dv2ma parametry self se nevol8'''

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def to_string(self):
        return "%.2f + %2fi" % (self.re, self.im)

    def size(self):
        return (self.re ** 2 + self.im ** 2) ** (1/2)

    def inc_parts(self, re, im):
        self.re += re
        self.im += im

    def inc(self, other):
        self.re = other.re
        self.im = other.im

    def __add__(self, other):
        return ComplexNumber(self.re+other.re, self.im + other.im)

    def __str__(self):
        return self.to_string()


if __name__ == "__main__":
    a = ComplexNumber(3, 4)
    '''print(a.to_string())
    print(a.size())'''
    b = ComplexNumber(1, 2)
    print(a.inc_parts(b))

    '''a.inc_parts(4, 2)
    c = a + b
    print(c.to_string())
    print(a.to_string())'''

'''Modul proo v7po4et skal8rn9ho sou4inu trida my_vector nezpomen na spravne pojmenovani
nemusi se nic importovat
je tam i testovaci kod'''
