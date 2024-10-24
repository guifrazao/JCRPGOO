class Validator:
    @staticmethod
    def verify_item_number(item_number):
        if isinstance(item_number, int) and 10000 <= item_number <= 99999999:
            return item_number
        else:
            print("O ID do item deve ter entre 5 e 8 dígitos!")
            raise ValueError("Item number")

    @staticmethod
    def verify_quantity(quantity):
        if quantity < 0:
            return 0
        return quantity

    @staticmethod
    def verify_price(price):
        if price < 0:
            return 0.0
        return price

    @staticmethod
    def verify_name(name):
        if len(name) >= 3:
            return name
        raise ValueError("Name")

    @staticmethod
    def verify_cpf(cpf):
        if len(cpf) == 11 and cpf.isnumeric():
            return cpf
        raise ValueError("CPF")

    @staticmethod
    def verify_tel(tel):
        if len(tel) == 11 and tel.isnumeric():
            return tel
        raise ValueError("Tel")
    
    @staticmethod
    def invalid_data_message(err):
        print(f"Erro: {err} inválido.")
