# roda.py

from validator import Validator_Roda

class Roda:
    def __init__(self, tamanho, pressao):
        if not Validator_Roda.verifyTamanho(tamanho):
            raise ValueError("Tamanho inválido para a roda.")
        if not Validator_Roda.verifyPressao(pressao):
            raise ValueError("Pressão inválida para a roda.")
        
        self.__tamanho = tamanho
        self.__pressao = pressao

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, tamanho):
        if not Validator_Roda.verifyTamanho(tamanho):
            raise ValueError("Tamanho inválido para a roda.")
        self.__tamanho = tamanho

    def getPressao(self):
        return self.__pressao

    def setPressao(self, pressao):
        if not Validator_Roda.verifyPressao(pressao):
            raise ValueError("Pressão inválida para a roda.")
        self.__pressao = pressao

    def __str__(self):
        return f"Tamanho: {self.__tamanho}, Pressão: {self.__pressao} PSI"
