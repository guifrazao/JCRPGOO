from validator import Validator
from owner import Owner

class Invoice:
    def __init__(self, item_number, description, quantity, price_per_item, owner: Owner):
        self.__item_number = Validator.verify_item_number(item_number)
        self.__description = description
        self.__quantity = Validator.verify_quantity(quantity)
        self.__price_per_item = Validator.verify_price(price_per_item)
        self.__owner = owner

    def __str__(self):
        return f"\nInformações Propritário\n{self.__owner}\n =--=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nInformações produto\nItem number: {self.__item_number}\nQuantity: {self.__quantity}\nPrice per item: {self.__price_per_item}"

    def set_item_number(self, item_number):
        self.__item_number = Validator.verify_item_number(item_number)

    def get_item_number(self):
        return self.__item_number

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_quantity(self, quantity):
        self.__quantity = Validator.verify_quantity(quantity)

    def get_quantity(self):
        return self.__quantity

    def set_price_per_item(self, price):
        self.__price_per_item = Validator.verify_price(price)

    def get_price_per_item(self):
        return self.__price_per_item

    def calculate_total(self):
        return self.__quantity * self.__price_per_item
