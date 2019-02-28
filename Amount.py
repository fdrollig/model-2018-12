class Amount:
    REPRODUCTION_VALUE = "Reproduction value"
    PRODUCT_QUANTITY = "B2B Product Quantity"
    def __init__(self, name, unit, quantity):
        self.name = name
        self.unit = unit
        self.quantity = quantity
    def add(self, anotherAmount):
        self.quantity = self.quantity + anotherAmount.quantity

