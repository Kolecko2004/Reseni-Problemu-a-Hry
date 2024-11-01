class MyVector:

    def __init__(self, vec):
        self.vecA = vec

    def get_vector(self):            
        return(self.vecA)

    def __mul__(self, other):
        vecB = other.get_vector()
        final = 0
        for i in range(len(self.vecA)):
            final += self.vecA[i] * vecB[i]
        return(final)
    
    def __add__(self, other): # soucet dvou vektoru
        vecB = other.get_vector()
        vecC = self.get_vector()
        for i in range(len(self.vecA)):
            vecC[i] = self.vecA[i] + vecB[i]
        return MyVector(vecC) 

    def norm(self):
        vec_sum = 0
        for i in range(len(self.vecA)):
            vec_sum += self.vecA[i]**2

        return(vec_sum**0.5)

if __name__ == "__main__":
    a = MyVector([3, -2, 3, 10])
    print(a)
    b = MyVector([4, 5, -6, 12])
    print(b)
    print(a.get_vector())
    print(b.get_vector())
    dot = a * b
    hello = a + b
    print(dot)
    print(hello)
    c = MyVector([1, 1, 2**0.5])
    print(c.norm())