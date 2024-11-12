seznam = [4, 5, 3, 2]

'''for i in seznam:
    print(i)

for i in range(len(seznam)):
    print(i, ", ", seznam[i])

funkce enumerate indexuje seznam
for i , item in enumerate(seznam):
    print(i, ", ", item)'''


def find_max(input_list):
    maximum = input_list[0]
    for i in range(1, len(input_list)):
        if (maximum < input_list[i]):
            maximum = input_list[i]
    return (maximum)


def find_better_max(input_list):
    if len(input_list) == 0:
        return (False)
    else:
        return (find_max(input_list))


if __name__ == "__main__":
    vec = [2, 3, 7, 4, 9, 10, 5, 8, 3]
    print(find_max(vec))
    vec1 = []
    print(find_better_max(vec1))
