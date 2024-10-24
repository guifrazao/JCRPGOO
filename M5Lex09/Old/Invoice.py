class Invoice:
    def __init__(self, item_number, description, quantity, price_per_item):
        self.__item_number = self.__validate_item_number(item_number)
        self.__description = description
        self.__quantity = self.__validate_quantity(quantity)
        self.__price_per_item = self.__validate_price(price_per_item) 

    def set_item_number(self, item_number):
        self.__item_number = self.__validate_item_number(item_number)

    def get_item_number(self):
        return self.__item_number

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_quantity(self, quantity):
        self.__quantity = self.__validate_quantity(quantity)

    def get_quantity(self):
        return self.__quantity

    def set_price_per_item(self, price):
        self.__price_per_item = self.__validate_price(price)

    def get_price_per_item(self):
        return self.__price_per_item

    def calculate_total(self):
        return self.__quantity * self.__price_per_item
    
    @staticmethod
    def __validate_item_number(item_number): 
        if not item_number.isdigit() or not (4 <= len(item_number) <= 8):
            raise ValueError("O número do item deve ser um número com 4 a 8 dígitos.")
        return item_number

    @staticmethod
    def __validate_quantity(quantity): 
        if quantity < 0:
            return 0
        return quantity

    @staticmethod
    def __validate_price(price):  
        if price < 0:
            return 0.0
        return price
