from rosemary import Item, update


# normal item

# test days_left


def test_normal_item_decreases_days_left():
    # Prepare for the test
    item = Item('Bread', days_left=3, quality=5)
    # Call to the tested function
    update(item)
    # Check the specification
    return item.days_left == 2


def test_normal_item_days_left_can_be_0():
    item = Item('Bread', days_left=1, quality=5)
    update(item)
    return item.days_left == 0


def test_normal_item_days_left_can_be_negative():
    item = Item('Bread', days_left=0, quality=5)
    update(item)
    return item.days_left == -1

    # test quality


def test_normal_item_decrease_quality():
    item = Item('Bread', days_left=3, quality=5)
    update(item)
    return item.quality == 4


def test_normal_item_quality_decrease_when_less_than_1_days_left():
    item = Item('Bread', days_left=0, quality=5)
    update(item)
    return item.quality == 3

def test_normal_item_quality_decrease_when_less_than_1_days_left_and_quality_is_0():
    item = Item('Bread', days_left=0, quality=0)
    update(item)
    return item.quality == 0 and item.days_left  == -1


def test_normal_item_quality_not_less_than_0():
    item = Item('Bread', days_left=5, quality=1)
    update(item)
    update(item)
    return item.quality == 0


def test_normal_item_qulatiy_when_50():
    item = Item('Bread', days_left=10, quality=50)
    update(item)
    return item.quality == 49


def test_name_is_not_changing_after_update():
    item_name = 'abcdefghchijklmopqrstuvwxyz'
    item = Item(item_name, days_left=2, quality=2)
    update(item)
    return item.name == item_name


def test_normal_item_quality_when_less_than_0_days():
    item = Item('Bread', days_left=-1, quality=30)
    update(item)
    return item.quality == 28


# test special items

    # DIAMOND

def test_diamon_item_name_change():
    item = Item('Diamond', days_left=10, quality=10)
    update(item)
    return item.name == 'Diamond'


def test_diamant_item_quality_not_changing():
    item = Item('Diamond', days_left=2, quality=100)
    update(item)
    return item.quality == 100


def test_diamant_item_days_left_not_changing():
    item = Item('Diamond', days_left=2, quality=100)
    update(item)
    return item.days_left == 2

    # CHEESE


def test_cheese_item_name_change():
    item = Item('Aged Brie', days_left=10, quality=10)
    update(item)
    return item.name == 'Aged Brie'


def test_cheese_item_quality_is_increasing():
    item = Item('Aged Brie', days_left=10, quality=5)
    update(item)
    return item.quality == 6


def test_cheese_item_quality_is_more_than_50():
    item = Item('Aged Brie', days_left=10, quality=49)
    update(item)
    update(item)
    return item.quality == 50


def test_cheese_item_days_left_less_than_0():
    item = Item('Aged Brie', days_left=0, quality=3)
    update(item)
    return item.quality == 4 and item.days_left == -1


def test_cheese_item_quality_0_incerease():
    item = Item('Aged Brie', days_left=10, quality=0)
    update(item)
    return item.quality == 1

    # TICKETS


def test_tickets_item_name_change():
    item = Item('Tickets', days_left=10, quality=10)
    update(item)
    return item.name == 'Tickets'


def test_tickets_item_quality_is_more_than_50_when_10_days():
    tickets_days_left = {11, 12, 13, 49, 48}
    for i in tickets_days_left:
        item = Item('Tickets', days_left=i, quality=50)
        update(item)
        return item.quality == 50


def test_tickets_item_quality_is_more_than_50_when_6_days():
    tickets_days_left = {6, 7, 8, 9, 10}
    for i in tickets_days_left:
        item = Item('Tickets', days_left=i, quality=50)
        update(item)
        return item.quality == 50


def test_tickets_item_quality_is_more_than_50_when_1_days():
    tickets_days_left = {1, 2, 3, 4, 5}
    for i in tickets_days_left:
        item = Item('Tickets', days_left=i, quality=50)
        update(item)
        return item.quality == 50


def test_tickets_item_quality_increase_more_than_10_days_left():
    tickets_days_left = {11, 12, 13, 49, 48}
    for i in tickets_days_left:
        item = Item('Tickets', days_left=i, quality=10)
        update(item)
        return item.quality == 10 + 1


def test_tickets_item_quality_increase_6_to_10_days_left():
    tickets_days_left = {6, 7, 8, 9, 10}
    for i in tickets_days_left:
        item = Item('Tickets', days_left=i, quality=10)
        update(item)
        return item.quality == 10 + 2


def test_tickets_item_quality_increase_1_to_5_days_left():
    tickets_days_left = {1, 2, 3, 4, 5}
    for i in tickets_days_left:
        item = Item('Tickets', days_left=i, quality=10)
        update(item)
        return item.quality == 10 + 3


def test_tickets_item_quality_drop_to_0_when_0_days_left():
    item = Item('Tickets', days_left=0, quality=10)
    update(item)
    return item.quality == 0
