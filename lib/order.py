class Order:
    def __init__(self, id, customer_name, order_date):
        self.id = id
        self.customer_name = customer_name
        self.order_date = order_date

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other: 'Order'):
        return self.__dict__ == other.__dict__
        #Debugging order_date type disparity
        return self.id == other.id and self.customer_name == other.customer_name and self.order_date == other.order_date
    
    # This method makes it look nicer when we print an Order    
    def __repr__(self):
        return f"Order({self.id}, {self.customer_name}, {self.order_date})"