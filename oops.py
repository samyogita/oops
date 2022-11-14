class Item:

    pay_rate = 0.8 #The pay rate after 20% discount
    def __init__(self, name:str, price:float, quantity=0):
        
        # Run validation to received arguements
        assert price >=0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        

        
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)

print(Item.__dict__) # All the attributes for class level are mapped in the dictionary and displayed
print(item1.__dict__) # All the attributes for instance level

