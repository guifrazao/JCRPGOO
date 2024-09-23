'''Implemente uma classe chamada Library que represente uma biblioteca virtual. Essa
classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar a
disponibilidade de um livro.'''

class Library:
    total_books = 0  # Atributo de classe para acompanhar o número total de livros na biblioteca

    def __init__(self):
        self.books = []  # Lista para armazenar os livros cadastrados
        self.loans = {}  # Dicionário para rastrear empréstimos, onde a chave é o título do livro e o valor é o nome do usuário

    # Método de classe para registrar um livro na biblioteca
    @classmethod
    def register_book(cls, title, author, copies):
        if cls.validate_copies(copies):  # Verifica se o número de cópias é válido usando um método estático
            book = {
                'title': title,
                'author': author,
                'copies': copies,
                'available': copies  # Inicialmente, todas as cópias estão disponíveis
            }
            cls.total_books += 1  # Atualiza o contador de livros totais da biblioteca
            return book
        else:
            print("Número de cópias inválido.")
            return None

    # Método para adicionar um livro à lista da biblioteca
    def add_book(self, title, author, copies):
        book = self.register_book(title, author, copies)  # Chama o método de classe para criar o livro
        if book:
            self.books.append(book)
            print("-" * 80)
            print(f"Livro '{title}' adicionado com sucesso.")

    # Método estático para validar se o número de cópias é um valor positivo
    @staticmethod
    def validate_copies(copies):
        return isinstance(copies, int) and copies > 0

    # Verifica se um livro está disponível para empréstimo
    def check_availability(self, title):
        for book in self.books:
            if book['title'] == title:
                return book['available'] > 0  # Retorna True se houver cópias disponíveis
        return False

    # Método para realizar o empréstimo de um livro
    def borrow_book(self, title, user):
        if self.check_availability(title):  # Verifica se o livro está disponível
            for book in self.books:
                if book['title'] == title:
                    book['available'] -= 1  # Diminui o número de cópias disponíveis
                    self.loans[title] = user  # Registra o empréstimo
                    print("-" * 80)
                    print(f"Livro '{title}' emprestado para {user}.")
                    break
        else:
            print("-" * 80)
            print(f"Desculpe, o livro '{title}' não está disponível no momento.")

    # Método para devolver um livro à biblioteca
    def return_book(self, title, user):
        if title in self.loans and self.loans[title] == user:  # Verifica se o livro está emprestado ao usuário correto
            for book in self.books:
                if book['title'] == title:
                    book['available'] += 1  # Aumenta o número de cópias disponíveis
                    del self.loans[title]  # Remove o empréstimo do registro
                    print("-" * 80)
                    print(f"Livro '{title}' devolvido por {user}.")
                    break
        else:
            print(f"Não há registro de empréstimo do livro '{title}' por {user}.")

    # Exibe todos os livros disponíveis na biblioteca
    def display_books(self):
        if not self.books:
            print("Nenhum livro disponível.")
        else:
            for book in self.books:
                print("-" * 80)
                print(f"Título: {book['title']}, Autor: {book['author']}, Cópias Disponíveis: {book['available']}")


