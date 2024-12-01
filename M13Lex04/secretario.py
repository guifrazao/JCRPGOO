from employee import Employee

class Secretario(Employee):
    def get_role(self):
        return "Secretário"

    def organize_documents(self):
        print(f"{self.get_name()} está organizando documentos.")
