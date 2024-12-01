from item_factory import ItemFactory

class Library:
    def __init__(self):
        # Usamos a Factory para criar os itens em vez de depender diretamente das classes concretas
        self.collections = {
            "Livro": [
                ItemFactory.create_item("Livro", "1984", 1949, "George Orwell"),
                ItemFactory.create_item("Livro", "O Senhor dos Anéis", 1954, "J.R.R. Tolkien"),
            ],
            "Revista": [
                ItemFactory.create_item("Revista", "National Geographic", 2023, "Edição de Novembro"),
                ItemFactory.create_item("Revista", "Superinteressante", 2023, "Edição Especial"),
            ],
            "DVD": [
                ItemFactory.create_item("DVD", "Matrix", 1999, "Lana Wachowski"),
                ItemFactory.create_item("DVD", "O Senhor dos Anéis", 2001, "Peter Jackson"),
            ],
            "CD": [
                ItemFactory.create_item("CD", "Thriller", 1982, "Michael Jackson"),
                ItemFactory.create_item("CD", "Back in Black", 1980, "AC/DC"),
            ],
        }

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
            print(f"  {i}. {item.get_details()}")  # Método get_details é polimórfico
        print("  0. Voltar")
        print("=" * 40)

    def rent_item(self, collection_type, item_index):  
        item = self.collections[collection_type].pop(item_index - 1)
        print(f"\n✅ Você alugou: {item.get_details()}")

    def run(self):  
        while True:
            self.display_menu()
            choice = input("👉 Sua escolha: ")
            if choice == "0":
                print("👋 Saindo do sistema. Até mais!")
                break
            try:
                collection_type = list(self.collections.keys())[int(choice) - 1]
                while True:
                    self.display_collection(collection_type)
                    sub_choice = input("👉 Escolha um item para alugar: ")
                    if sub_choice == "0":
                        break
                    try:
                        self.rent_item(collection_type, int(sub_choice))
                    except (IndexError, ValueError):
                        print("⚠️ Escolha inválida. Tente novamente.")
            except (IndexError, ValueError):
                print("⚠️ Escolha inválida. Tente novamente.")

# A Library agora depende da ItemFactory e da abstração ItemCollection, e não diretamente das implementações concretas (Book, Magazine, DVD, CD).