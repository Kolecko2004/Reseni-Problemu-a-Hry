a = [1, 2, 3]
b = a
a[0] = 9
print (a, b)

def increment_pure_funvtion(x):
    v = []
    for item in x:
        v.append(item + 1)
    return v

def increment_modifier(x):
    for i in range(len(x)):
        x[i] += 1
    return x

if __name__ == '__main__':
    a = [1, 2, 3]
    b1 = increment_pure_funvtion(a)
    d0 = a == b1
    b2 = increment_modifier(a)
    d1 = b1 == b2
    d2 = a == b1
    print(d0, d1, d2)

    c = [2, 3, 4, 512, 65, 76, 98, 0 ]
    c.sort()
    print(c)
    print(a + [1])
    print(a)