from lib.item import *

class ItemRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM items")
        return [
            Item(row["id"], row["name"], row["unit_price"],
                row["quantity"], row["order_id"])
                for row in rows
        ]
    
    def find(self, item_id):
        rows = self._connection.execute(
            "SELECT * FROM items WHERE id = %s", [item_id])
        row = rows[0]
        return Item(1, 'air bison whistle', 5, 1, 1)
    
    def create(self, item) -> None:
        self._connection.execute(
            "INSERT INTO items (name, unit_price, quantity, order_id) VALUES (%s, %s, %s, %s)",
            [item.name, item.unit_price, item.quantity, item.order_id])