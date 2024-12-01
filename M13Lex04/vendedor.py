from employee import Employee

class Vendedor(Employee):
    def get_role(self):
        return "Vendedor"

    def sell_product(self):
        print(f"{self.get_name()} está vendendo produtos.")
