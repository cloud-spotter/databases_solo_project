from lib.order import *
from lib.order_repository import *

'''
#all returns a list of all records from the seed data
'''
def test_all(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    orders = repository.all()
    
    # Debugging this AssertionError:
    # FAILED tests/test_order_repository.py::test_all - AssertionError: assert Order(1, Aang, 1870-08-01) == Order(1, Aang, 1870-08-01)
    # print('aaa',type( orders[0].order_date))
    # assert orders[0] == Order(1, 'Aang', '1870-08-01') 
    # Datatype disparity - SQL order_date = date type. 
    # Changed shop_manager.sql file L15 order_date type to text so python recognises both as equal.
    
    assert orders == [
        Order(1, 'Aang', '1870-08-01'),
        Order(2, 'Katara', '1870-06-01')
    ]

'''
#find returns a single order
where the order matches the query condition
'''

def test_find(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    result = repository.find(1)
    result == Order(1, 'Aang', '1870-08-01')

'''
#create makes a new order record entry in the orders table
and the new order appears in the table when #all is called
'''

def test_create(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    order = Order(None, 'Aang', '1870-08-01')
    repository.create(order)
    
    assert repository.all() == [
        Order(1, 'Aang', '1870-08-01'),
        Order(2, 'Katara', '1870-06-01'),      
        Order(3, 'Aang', '1870-08-01')
    ]