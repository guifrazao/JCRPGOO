from .validator import Validator_Owner

class Owner:
    def __init__(self, name, cpf, tel):
        if not Validator_Owner.verifyName(name):
            raise Exception("Name")
        if not Validator_Owner.verifyCPF(cpf):
            raise Exception("CPF")
        if not Validator_Owner.verifyTel(tel):
            raise Exception("Tel")

        self.__name = name
        self.__cpf = cpf
        self.__tel = tel
        self.__invoice = None  # Atributo para armazenar a fatura

    def set_invoice(self, invoice):
        """Associar uma fatura ao proprietário."""
        self.__invoice = invoice

    def get_invoice(self):
        """Retornar a fatura associada ao proprietário."""
        return self.__invoice

    def get_name(self):
        """Retornar o nome do proprietário."""
        return self.__name

    def set_name(self, name):
        """Definir o nome do proprietário, se válido."""
        if not Validator_Owner.verifyName(name):
            raise Exception("Nome inválido")
        self.__name = name

    def get_cpf(self):
        """Retornar o CPF do proprietário."""
        return self.__cpf

    def set_cpf(self, cpf):
        """Definir o CPF do proprietário, se válido."""
        if not Validator_Owner.verifyCPF(cpf):
            raise Exception("CPF inválido")
        self.__cpf = cpf

    def get_tel(self):
        """Retornar o telefone do proprietário."""
        return self.__tel

    def set_tel(self, tel):
        """Definir o telefone do proprietário, se válido."""
        if not Validator_Owner.verifyTel(tel):
            raise Exception("Telefone inválido")
        self.__tel = tel

    def __str__(self):
        formatted_cpf = f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}"
        formatted_tel = f"({self.__tel[:2]}) {self.__tel[2:7]}-{self.__tel[7:]}"
        return f"\nName: {self.__name}\nCPF: {formatted_cpf}\nTel: {formatted_tel}"
