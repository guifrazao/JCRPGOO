class Validator_Bicycle:

    @staticmethod
    def verifyVelocidade(velocidade):
        return velocidade >= 0
    
    @staticmethod
    def verifyCadencia(cadencia):
        return cadencia >= 0

    @staticmethod
    def verifyMarcha(marcha):
        return 1 <= marcha <= 18

    @staticmethod
    def verifyNumeroSerie(numero_serie):
        return numero_serie > 1000
    
    @staticmethod
    def invalidDataMessage(err):
        print(f"Erro: {err} inválido.")




class Validator_Owner:

    @staticmethod
    def verifyName(name):
        return len(name) >= 3
    
    @staticmethod
    def verifyCPF(cpf):
        return len(cpf) == 11 and cpf.isnumeric()




class invalidDataMessage:

    @staticmethod
    def invalidDataMessage(err):
        print(f"Erro: {err} inválido.")