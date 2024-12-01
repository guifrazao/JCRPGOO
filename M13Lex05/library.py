from user import User
from book import Book
from magazine import Magazine
from dvd import DVD
from cd import CD

class Library:
    def __init__(self):
        self.collections = {
            "Livro": [
                Book("1984", 1949, "George Orwell"),
                Book("O Senhor dos Anéis", 1954, "J.R.R. Tolkien"),
            ],
            "Revista": [
                Magazine("National Geographic", 2023, "Edição de Novembro"),
                Magazine("Superinteressante", 2023, "Edição Especial"),
            ],
            "DVD": [
                DVD("Matrix", 1999, "Lana Wachowski"),
                DVD("O Senhor dos Anéis", 2001, "Peter Jackson"),
            ],
            "CD": [
                CD("Thriller", 1982, "Michael Jackson"),
                CD("Back in Black", 1980, "AC/DC"),
            ],
        }
        self.users = []  # Lista para armazenar os usuários

    def add_user(self, user):
        """Adiciona um novo usuário à biblioteca."""
        self.users.append(user)

    def display_menu(self):
        print("\n🌟 Bem-vindo ao Sistema de Biblioteca 🌟")
        print("=" * 40)
        print("📋 Escolha uma opção:")
        for i, collection_type in enumerate(self.collections.keys(), start=1):
            emoji = {"Livro": "📚", "Revista": "📰", "DVD": "📀", "CD": "🎵"}
            print(f"  {emoji[collection_type]} {i}. {collection_type}")
        print("  🚪 0. Sair")
        print("=" * 40)

    def display_collection(self, collection_type):
        items = self.collections[collection_type]
        print(f"\n--- 📂 Acervo de {collection_type}s ---")
        for i, item in enumerate(items, start=1):
            print(f"  {i}. {item.get_details()}")
        print("  0. Voltar")
        print("=" * 40)

    def rent_item(self, user, collection_type, item_index):
        """Aluga um item para um usuário específico."""
        item = self.collections[collection_type].pop(item_index - 1)
        user.rent(item)
        print(f"\n✅ {user.name} alugou: {item.get_details()}")

    def return_item(self, user, collection_type, item_index):
        """Devolve um item para a biblioteca e remove do histórico do usuário."""
        item = user.rented_items[item_index - 1]
        user.return_item(item)
        self.collections[collection_type].append(item)

    def run(self):
        # Criando usuários
        user1 = User("Alice")
        user2 = User("Bob")
        self.add_user(user1)
        self.add_user(user2)

        while True:
            print("\nSelecione o usuário:")
            for i, user in enumerate(self.users, start=1):
                print(f"  {i}. {user.name}")
            print("  0. Sair")
            user_choice = input("👉 Sua escolha: ")
            if user_choice == "0":
                print("👋 Saindo do sistema. Até mais!")
                break
            try:
                user = self.users[int(user_choice) - 1]
                while True:
                    self.display_menu()
                    choice = input("👉 Sua escolha: ")
                    if choice == "0":
                        break
                    try:
                        collection_type = list(self.collections.keys())[int(choice) - 1]
                        while True:
                            self.display_collection(collection_type)
                            sub_choice = input("👉 Escolha um item para alugar: ")
                            if sub_choice == "0":
                                break
                            try:
                                self.rent_item(user, collection_type, int(sub_choice))
                            except (IndexError, ValueError):
                                print("⚠️ Escolha inválida. Tente novamente.")
                    except (IndexError, ValueError):
                        print("⚠️ Escolha inválida. Tente novamente.")
                user.show_rented_items()
            except (IndexError, ValueError):
                print("⚠️ Escolha inválida. Tente novamente.")
