from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, id_funcionario, salario): 
        self.__nome = nome 
        self.__id_funcionario = id_funcionario 
        self.__salario = salario

    @abstractmethod 
    def obter_cargo(self): 
        pass 
    
    def obter_nome(self): 
        return self.__nome 
    
    def obter_id_funcionario(self): 
        return self.__id_funcionario 
    
    def obter_salario(self): 
        return self.__salario 
    
    def __str__(self): 
        return f"Nome: {self.__nome}\nID: {self.__id_funcionario}\nSalário: R${self.__salario:.2f}"
