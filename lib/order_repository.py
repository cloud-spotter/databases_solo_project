from lib.order import *

class OrderRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM orders")
        return [
            Order(row["id"], row["customer_name"], row["order_date"])
            for row in rows
        ]
    
    def find(self, order_id):
        rows = self._connection.execute(
            "SELECT * FROM orders WHERE id = %s", [order_id])
        row = rows[0]
        return Order(row["id"], row["customer_name"], row["order_date"])
    
    def create(self, order) -> None:
        self._connection.execute(
            "INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)", 
            [order.customer_name, order.order_date]
        )
        return None