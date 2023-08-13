class Item:
    def __init__(self, id, name, unit_price, quantity, order_id) -> None:
        self.id = id
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
        self.order_id = order_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__    

    def __repr__(self) -> str:
        return f"Item({self.id}, {self.name}, {self.unit_price}, {self.quantity}, {self.order_id})"
