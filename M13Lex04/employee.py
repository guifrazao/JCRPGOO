from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id, salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    @abstractmethod
    def get_role(self):
        pass

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return f"Name: {self.__name}\nID: {self.__employee_id}\nSalary: ${self.__salary:.2f}"
