'''
5.11.2024
Generatory - efektivni zpusob jak vyrabet sekvence pro smycky
je to lepsi nez bytvorit seznam a potom ho iterovat
kazdy prvek vznikne az kdyz ho budeme potrebovat
mensi zatez na pamet
zprehledneni programu
YIELD - klicove slovo
generator nam dava zpusob jak vytvret sadu elementu pokdu jsou potreba 
yield funguje jako return ale potom si funkce pamatuje kdy v tom prubehu skolncila a ceka na dalsi zavolani
a potom se to muze pouzit jako 

for elem in generator():
    do something
    
for nahore vlastne porad vola next, next atd...
muzu z toho vytvorit nejaky objekt napriklad list

list = (generated)

dalsi je RANGE ten pouzivame hodne u FOR
nema next()
muzeme ho indexovat


- PISKVORKY
    - piskvorky se dobre pouziji na dekompozici
    - rozkladam program na tak jednoduche casti ze kdyz ty casti programuju tak kazda samostatne je uplne trivialni
    - prvni verze kodu nikdy neorezije
    - je lepsi zlepsovat casti kodu nez cely kod najednou
    - pokud me nuti neco napsat komentar do kodu
        - pokud se toto stane tak je nejlepsi kdyz zmenime kod tak aby nebzl potreba zadny komentar
    - volani funkce neni zadarmo, ale program vetsinou zpomaluji jine veci
    - BOOK - the art of unix programing
    
'''


def squared_sequence(start, stop, step=1):  # fin=bonacio sekvence funkce
    num = start
    while num < stop:
        yield num ** 2
        num += step


def generate_fib(n):
    a, b = (0, 1)
    for _ in range(n):
        yield a
        a, b = (b, a + b)


if __name__ == '__main__':
    for num in generate_fib(10):
        print(num)

    s1 = squared_sequence(10, 15, 2)
    s2 = (x ** 2 for x in range(10, 15, 2))  # list comprehension

    r1 = s1 == s2
    r2 = list(s1) == list(s2)

    print(r1)
    print(r2)
