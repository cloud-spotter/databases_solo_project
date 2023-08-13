from lib.item_repository import *
from lib.item import *

'''
#all returns a list of all records from the seed data
'''
def test_all(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    items = repository.all()
    assert items == [
        Item(1, 'air bison whistle', 5, 1),
        Item(2, 'waterbending scroll', 50, 1)
    ]

'''
#find returns a single item
where the item matches the query condition
'''

def test_find(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    result = repository.find(1)
    result == Item(1, 'air bison whistle', 5, 1)

'''
#create makes a new item record entry in the items table
and the new item appears in the table when #all is called
'''

def test_create(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    item = Item(3, 'boomerang', 12, 1)
    repository.create(item)
    
    assert repository.all() == [
        Item(1, 'air bison whistle', 5, 1),
        Item(2, 'waterbending scroll', 50, 1),
        Item(3, 'boomerang', 12, 1)
    ]