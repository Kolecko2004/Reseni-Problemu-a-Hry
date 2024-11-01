import random

x = 1000000
isLate = 0
bus = ["Bus", 358, 362]
child = ["child", 355, 361]

for i in range (x):
    timeBus = random.randrange(bus[1], bus[2] + 1)
    timeChild = random.randrange(child[1], child[2] + 1)
    if (timeChild > timeBus):
        isLate += 1

percentage = isLate / (x / 100)
print(bus[1], bus[2])
print(child[1], child[2])
print(f'{percentage}%')