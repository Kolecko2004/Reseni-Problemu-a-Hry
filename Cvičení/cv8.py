# testing framework
'''
Zbozi je instance class Item
item has these: name, daysleft, quality
Specialni predmety
    - Aged Brie
    - Diamond
    - Tickets

Funkce update na konci kazdeho dne
    - snizi kvalitu a daysleft
    - funkce je modifikator
    
Pravidla pro funkci update
    - vzdy dostane instanci zbozi se spravnymi parametry
    - ma udelat: 
        - nazev se nemeni
        - kvalita neni nikdy mensi nez nula nebo vetsi nez 50
        - kvalita i trvanlivost se zmeni
        - 2x rychleji 
        - diamanty nestraceji ani kvalitu ani trvanlivost
        - zrajici syr kvalitu ziskava kazdym dnem
        - tickets cena se meni jinak nez normalne

test rosmery.py
    - sada testu
    - testovaci funkce se pisou co nejkratsi (testujou jenom jednu vec)
    - vsechny funkce budou 'test_'
    - vraci TRUE a FALSE - False je ze je chyba
'''