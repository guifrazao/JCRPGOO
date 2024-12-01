from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year, price):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price

    @abstractmethod
    def get_vehicle_type(self):
        pass

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__year} {self.__brand} {self.__model}, Price: ${self.__price:.2f}"

    