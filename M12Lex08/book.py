from product import Product

class Book(Product):
    def __init__(self, name, price, description, author):
        super().__init__(name, price, description)
        self.author = author

    def get_description(self):
        return f"{super().get_description()}: {self.description} Autor: {self.author}"

