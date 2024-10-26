from validator import Validator_invoice
from owner import Owner

class Invoice:
    def __init__(self, item_number, description, quantity, price_per_item, owner: Owner):
        if not Validator_invoice.verifyItem_number(item_number):
            raise Exception("Item number")
        if not Validator_invoice.verifyQuantity(quantity):
            raise Exception("Quantity")
        if not Validator_invoice.verifyPrice(price_per_item):
            raise Exception("Price per item")
        self.__item_number = item_number
        self.__description = description
        self.__quantity = quantity
        self.__price_per_item = price_per_item
        self.__owner = owner

    def __str__(self):
        return f"\nInformações Proprietário\n{self.__owner}\n =--=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nInformações produto\nItem number: {self.__item_number}\nQuantity: {self.__quantity}\nPrice per item: {self.__price_per_item}"

    def calculate_total(self):
        return self.__quantity * self.__price_per_item
