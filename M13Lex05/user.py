class User:
    """
    Representa um usuário da biblioteca.
    Um usuário pode alugar múltiplos itens da biblioteca.
    """
    def __init__(self, name):
        self.name = name
        self.rented_items = []  # Lista para armazenar os itens alugados

    def rent(self, item):
        """Aluga um item e adiciona ao histórico do usuário."""
        self.rented_items.append(item)

    def return_item(self, item):
        """Devolve um item e o remove do histórico do usuário."""
        if item in self.rented_items:
            self.rented_items.remove(item)
            print(f"✅ {self.name} devolveu: {item.get_details()}")
        else:
            print(f"⚠️ {self.name} não tem o item: {item.get_details()}")

    def show_rented_items(self):
        """Exibe os itens alugados pelo usuário."""
        if not self.rented_items:
            print(f"{self.name} não alugou nenhum item.")
        else:
            print(f"\nItens alugados por {self.name}:")
            for item in self.rented_items:
                print(item.get_details())
