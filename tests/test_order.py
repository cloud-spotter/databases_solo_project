from lib.order import *

'''
Order constructs with id & user_name
'''
def test_order_constructs():
    order = Order(1, 'Aang', '1870-08-01')
    assert order.id == 1
    assert order.customer_name == 'Aang'
    assert order.order_date == '1870-08-01'

'''
Check two identical order records register as equal
'''
def test_two_orders_are_equal():
    order1 = Order(1, 'Aang', '1870-08-01')
    order2 = Order(1, 'Aang', '1870-08-01')
    assert order1 == order2

'''
Format orders nicely
'''
def test_format_orders_nicely():
    order = Order(1, 'Aang', '1870-08-01') 
    assert str(order) == 'Order(1, Aang, 1870-08-01)'