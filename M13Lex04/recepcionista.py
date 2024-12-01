from employee import Employee

class Recepcionista(Employee):
    def get_role(self):
        return "Recepcionista"

    def greet_visitors(self):
        print(f"{self.get_name()} está cumprimentando os visitantes.")
