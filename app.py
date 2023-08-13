from lib.database_connection import DatabaseConnection
from lib.order_repository import *
from lib.order import *
from lib.item_repository import *
from lib.item import *

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/shop_manager.sql")

# Retrieve all orders
orders_repository = OrderRepository(connection)
orders = orders_repository.all()

for order in orders:
    print(order)         

# Retrieve all items
item_repository = ItemRepository(connection)  
items = item_repository.all()

# # List them out
for item in items:                            
    print(item)

## Functions:
#welcome

## manage_items
#list_all_shop_items
#create_new_item

## manage_orders
#list_all_orders
#create_new_order 

def run():
    print("Welcome to the shop management program")
    management_action = input('''What would you like to do?
        1 = list all shop items
        2 = create a new item
        3 = list all orders
        4 = create a new order
        Enter choice: ''')

    if int(management_action) == 1:
        print("Shop items: ")
        items = ItemRepository(connection).all()
        for item in items:
            print(f"Item {item.id}: {item.name}, unit price: {item.unit_price}, quantity: {item.quantity}")

    elif int(management_action) == 2:
        new_item_name = input("Enter item name: ")
        new_item_unit_price = input("Enter item unit price: ")
        new_item_quantity = input("Enter item quantity: ")
        
        item_repository = ItemRepository(connection)
        item_repository.create(Item(None, new_item_name, new_item_unit_price, new_item_quantity))
        print(item_repository.all())  #THIS DOESN'T 

    elif
        







print(run())

