'''
Crie uma classe chamada VirtualStore que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho
de compras, aplicar descontos e calcular o valor total da compra.
'''

class VirtualStore:
    total_products = 0  # Atributo de classe para contar produtos

    def __init__(self):
        self.products = [] 
        self.cart = {}
        self.discount = 0

    @classmethod
    def create_product(cls, name, price, description, quantity):
        if cls.validate_price(price) and cls.validate_quantity(quantity):
            product = {
                'name': name,
                'price': price,
                'description': description,
                'quantity': quantity,
            }
            cls.total_products += 1  # Incrementa o total de produtos
            return product
        else:
            print("Produto inválido.")
            return None

    @staticmethod
    def validate_price(price):
        return isinstance(price, (int, float)) and price >= 0

    @staticmethod
    def validate_quantity(quantity):
        return isinstance(quantity, int) and quantity >= 0

    def register_products(self, name, price, description, quantity):
        product = self.create_product(name, price, description, quantity)
        if product:
            self.products.append(product)

    def add_cart(self, name, quantity):
        for product in self.products:
            if product['name'] == name:
                if product['quantity'] >= quantity:
                    if name in self.cart:
                        self.cart[name] += quantity
                    else:
                        self.cart[name] = quantity
                    product['quantity'] -= quantity
                else:
                    print("Estoque insuficiente para esse produto.")
                break
        else:
            print("Produto não encontrado.") 

    def remove_cart(self, name, quantity):
        if name in self.cart:
            if self.cart[name] >= quantity:
                self.cart[name] -= quantity  # Diminui a quantidade no carrinho
                if self.cart[name] == 0:
                    del self.cart[name]  # Remove o produto do carrinho se a quantidade for zero
                # Atualiza o estoque do produto na loja
                for product in self.products:
                    if product['name'] == name:
                        product['quantity'] += quantity
                        break
            else:
                print(f"Quantidade no carrinho é menor que {quantity}.")
        else:
            print("Produto não está no carrinho.")

    def view_cart(self):
        if not self.cart:
            print("O carrinho está vazio.")
        else:
            total_cart_value = 0
            print("Itens no carrinho:")
            for name, quantity in self.cart.items():
                for product in self.products:
                    if product['name'] == name:
                        item_total = product['price'] * quantity
                        total_cart_value += item_total
                        print(f"Produto: {name}, Quantidade: {quantity}, Preço Total: R$ {item_total:.2f}")
                        break
            print(f"Total geral do carrinho: R$ {total_cart_value:.2f}")

    def apply_discount(self, tipo, valor):
        if tipo == 'percentual':
            if 0 <= valor <= 100:
                self.discount = valor / 100
            else:
                print("Desconto percentual inválido.")
        
        elif tipo == 'valor':
            if valor > 0:
                self.discount = valor  
            else:
                print("Desconto inválido.")
        
        else:
            print("Tipo de desconto inválido. Utilize 'percentual' ou 'valor' ")
    
    def calculate_total(self):
        total = 0
        # Soma o valor total dos produtos no carrinho
        for name, quantity in self.cart.items():
            for product in self.products:
                if product['name'] == name:
                    total += product['price'] * quantity

        # Aplica o desconto
        if isinstance(self.discount, float):  # Se for um desconto percentual
            total -= total * self.discount  # Aplica o desconto percentual
        elif isinstance(self.discount, int):  # Se for um desconto fixo
            total -= self.discount  # Aplica o desconto fixo

        # Garante que o total não seja negativo
        if total < 0:
            total = 0

        return total

    def display_products(self):
        if not self.products:
            print("Nenhum produto disponível.")
        else:
            for product in self.products:
                print("-" * 30)
                print(f"Produto: {product['name']}")
                print(f"Preço: R$ {product['price']:.2f}")
                print(f"Descrição: {product['description']}")
                print(f"Quantidade disponível: {product['quantity']}")
                print("-" * 30)  # Um divisor para separar os produtos


