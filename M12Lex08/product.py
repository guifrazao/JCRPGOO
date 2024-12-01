class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price
    
    def get_description(self):
        return "Produto de informática"
