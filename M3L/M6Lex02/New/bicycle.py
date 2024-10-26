from validator import Validator_Bicycle
from validator import invalidDataMessage
from owner import Owner
from roda import Roda

class Bicycle:
    def __init__(self, velocidade, cadencia, marcha, nmr_serie, owner: Owner, roda: list[Roda]):
        if not Validator_Bicycle.verifyVelocidade(velocidade):
            raise ValueError("VELOCIDADE")
        if not Validator_Bicycle.verifyCadencia(cadencia):
            raise ValueError("CADÊNCIA")
        if not Validator_Bicycle.verifyMarcha(marcha):
            raise ValueError("MARCHA")
        if not Validator_Bicycle.verifyNumeroSerie(nmr_serie):
            raise ValueError("NÚMERO DE SÉRIE")
        
        self.__velocidade = velocidade
        self.__cadencia = cadencia
        self.__marcha = marcha
        self.__nmr_serie = nmr_serie
        self.__owner = owner
        self.__roda = roda

    def __str__(self):
        roda_info = "\n".join(str(wheel) for wheel in self.__roda)
        return f"""         Informações Proprietario:
--------------------------------------------
{self.__owner}
=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-=-=--==-=-=-
        Informações Bicicleta:
--------------------------------------------
Velocidade: {self.__velocidade}
Cadência: {self.__cadencia}
Marcha Atual: {self.__marcha}
Número de série: {self.__nmr_serie}
=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-=-=--==-=-=-
        Informações Roda:
--------------------------------------------
{roda_info}
--------------------------------------------"""
    
    def getVelocidade(self):
        return self.__velocidade

    def setVelocidade(self, velocidade):
        if not Validator_Bicycle.verifyVelocidade(velocidade):
            invalidDataMessage("velocidade")
        else:
            self.__velocidade = velocidade

    def getCadencia(self):
        return self.__cadencia

    def setCadencia(self, cadencia):
        if not Validator_Bicycle.verifyCadencia(cadencia):
            invalidDataMessage("cadência")
        else:
            self.__cadencia = cadencia

    def getMarcha(self):
        return self.__marcha

    def setMarcha(self, marcha):
        if not Validator_Bicycle.verifyMarcha(marcha):
            invalidDataMessage("march")
        else:
            self.__marcha = marcha

    def getNmr_serie(self):
        return self.__nmr_serie

    def setNmr_serie(self, nmr_serie):
        if not Validator_Bicycle.verifyNumeroSerie(nmr_serie):
            invalidDataMessage("Número de série")
        else:
            self.__nmr_serie = nmr_serie

    def getOwner(self) -> Owner:
        return self.__owner

    def setOwner(self, owner: Owner):
        self.__owner = owner

    def getroda(self) -> list[Roda]:
        return self.__roda

    def setroda(self, roda: list[Roda]):
        self.__roda = roda

    def velocidade_relativa(self, outra_bike):
        return abs(self.__velocidade - outra_bike.getVelocidade())
