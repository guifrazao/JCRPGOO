from .owner import Owner
from .validator import Validator_invoice

class Invoice:
    def __init__(self, item_number, description, quantity, price_per_item, owner: Owner):
        if not Validator_invoice.verifyItem_number(item_number):
            raise Exception("Item number")
        if not Validator_invoice.verifyQuantity(quantity):
            raise Exception("Quantity")
        if not Validator_invoice.verifyPrice(price_per_item):
            raise Exception("Price per item")
        
        self.__item_number = Validator_invoice.verifyItem_number(item_number)
        self.__description = description
        self.__quantity = Validator_invoice.verifyQuantity(quantity)
        self.__price_per_item = Validator_invoice.verifyPrice(price_per_item)
        self.__owner = owner
        self.__owner.set_invoice(self)  # Associação bilateral

    def __str__(self):
        return (f"\nInformações Proprietário\n{self.__owner}"
                f"\n=--=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                f"Informações produto\nItem number: {self.__item_number}\n"
                f"Quantity: {self.__quantity}\nPrice per item: {self.__price_per_item}")

    def calculate_total(self):
        return self.__quantity * self.__price_per_item
