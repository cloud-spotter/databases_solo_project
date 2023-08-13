from lib.item import *

'''
Contructs with id, name, unit_price, quantity, item_id
'''
def test_item_constructs():
    item = Item(1, 'air bison whistle', 5, 1, 1)
    assert item.id == 1
    assert item.name == 'air bison whistle'
    assert item.unit_price == 5
    assert item.quantity == 1
    assert item.order_id == 1

'''
Check two identical item records register as equal
'''
def test_two_items_are_equal():
    item1 = Item(1, 'air bison whistle', 5, 1, 1)
    item2 = Item(1, 'air bison whistle', 5, 1, 1)
    assert item1 == item2

# '''
# Format items nicely
# '''
def test_format_items_nicely():
    item = Item(1, 'air bison whistle', 5, 1, 1)
    assert str(item) == 'Item(1, air bison whistle, 5, 1, 1)'