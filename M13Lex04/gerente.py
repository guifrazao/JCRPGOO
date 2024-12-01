from employee import Employee

class Gerente(Employee):
    def get_role(self):
        return "Gerente"

    def manage_team(self):
        print(f"{self.get_name()} está gerenciando a equipe.")
