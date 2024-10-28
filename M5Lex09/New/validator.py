class Validator_invoice:

    @staticmethod
    def verifyItem_number(item_number):
        # Verifica se o número do item é um inteiro e se tem entre 5 e 8 dígitos
        if isinstance(item_number, int) and 10000 <= item_number <= 99999999:
            return True
        else:
            print("O ID do item deve ter entre 5 e 8 dígitos!")
            return False


    @staticmethod
    def verifyQuantity(quantity): 
        if quantity < 0:
            return 0
        return quantity

    @staticmethod
    def verifyPrice(price):  
        if price < 0:
            return 0.0
        return price
    

class Validator_Owner:

    @staticmethod
    def verifyName(name):
        return len(name) >= 3
    
    @staticmethod
    def verifyCPF(cpf):
        return len(cpf) == 11 and cpf.isnumeric()
    
    @staticmethod
    def verifyTel(tel):
        return len(tel) == 11 and tel.isnumeric()
    

class invalidDataMessage:

    @staticmethod
    def invalidDataMessage(err):
        print(f"Erro: {err} inválido.")