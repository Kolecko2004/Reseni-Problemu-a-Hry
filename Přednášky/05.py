'''
Prednaska cislo 5

- uloha reversi
    - klasicka deskova hra
    - hrací deska 8 x 8
    - 2 hráči
    - Střídání tahů
    - Tah - hráč přidá na desku kámen své barvy
    - Konec hry - žádný hráč nemůže přidat kámen
    - Vítěz - vyšší počet kamenů své barvy

- Který tah převrátí nejvíce kamenů (taktika?)

- Mechanical Turk (History) - hraní šachu robotem - robot to vlastně vůbec nebyl

- Práce s 2D poli (při reversi)
    - Indexování
    - Mělké a hluboké kopie

- Množiny
    - a = {1, 2, 3, 3}
    - print(a) === ({1, 2, 3})
    - Vyřadí se prvky, které tam jsou vícekrát
    - & je jako průnik dvou množin
    - if element IN array - in hlídá jestli prvek je v množině
    - .add() and .remove()
    - Frozenset() - množina se už nebude měnit, už se s tím nemůže hýbat

- List Comprehension
    - Generátor seznamu na základě nějaké podmínky
    '''

import time
a = [x ** 2 for x in range(-10, 10)]
print(a)

fruit = ['apple', 'banana', 'lemon', 'plum', 'watermelon']

b = [f for f in fruit if 'a' in f]
print(b)

'''
- Narozeninový problém
    - Od 23 osob je větší šance, že budou mít dvě osoby stejné narozeniny, než že žádné nebudou mít stejné narozeniny

- Optimalizace
    - Vytvořit více variant a při testech vybrat tu nejrychlejší
    - 3 * [1, 2] == [1, 2, 1, 2, 1, 2]
    - Jak měřit rychlost kódu
    '''

t_start = time.time()

a = [x ** 2 for x in range(-10, 10)]
print(a)

fruit = ['apple', 'banana', 'lemon', 'plum', 'watermelon']

b = [f for f in fruit if 'a' in f]
print(b)

print(f'Time spent doing the program {time.time() - t_start}')

'''
- Garbage colector - pokud proměnou už nepoužijeme tak smažeme data
'''
