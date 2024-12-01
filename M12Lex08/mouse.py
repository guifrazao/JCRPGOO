from product import Product

class Mouse(Product):
    def __init__(self, name, price, description, type_):
        super().__init__(name, price, description)
        self.type = type_

    def get_description(self):
        return f"{super().get_description()}: {self.description} Tipo: {self.type}"
