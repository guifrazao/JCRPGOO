from validator import Validator_invoice
from validator import invalidDataMessage
from owner import Owner

class Invoice:
    def __init__(self, item_number, description, quantity, price_per_item, owner: Owner):

        if not Validator_invoice.verifyItem_number(item_number):
            raise Exception ("Item number")
        if not Validator_invoice.verifyQuantity(quantity):
            raise Exception ("Quantity")
        if not Validator_invoice.verifyPrice(price_per_item):
            raise Exception ("Price per item")
        
        self.__item_number = Validator_invoice.verifyItem_number(item_number)
        self.__description = description
        self.__quantity = Validator_invoice.verifyQuantity(quantity)
        self.__price_per_item = Validator_invoice.verifyPrice(price_per_item) 
        self.__owner = owner

    def __str__(self):
        return f"\nInformações Propritário\n{self.__owner}\n =--=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nInformações produto\nItem number: {self.__item_number}\nQuantity: {self.__quantity}\nPrice per item: {self.__price_per_item}"

    def set_item_number(self, item_number):
        if not Validator_invoice.verifyItem_number(item_number):
            invalidDataMessage("Item number")

    def get_item_number(self):
        return self.__item_number

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_quantity(self, quantity):
        self.__quantity = Validator_invoice.verifyQuantity(quantity)

    def get_quantity(self):
        return self.__quantity

    def set_price_per_item(self, price):
        self.__price_per_item = Validator_invoice.verifyPrice(price) 

    def get_price_per_item(self):
        return self.__price_per_item

    def calculate_total(self):
        return self.__quantity * self.__price_per_item
    

