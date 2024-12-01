"""
Implemente um sistema de Biblioteca com os tipos de acervo (livro, revista, DVD, CD,
etc.), evidenciando a classe Collection como uma classe abstrata.
"""
from library import Library
from cd import CD
from livro import Book
from revista import Magazine
from dvd import DVD

def main():
    library = Library()
    
    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Adicionar Livro")
        print("2. Adicionar Revista")
        print("3. Adicionar DVD")
        print("4. Adicionar CD")
        print("5. Listar Coleções")
        print("6. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            title = input("Título do Livro: ")
            year = int(input("Ano: "))
            author = input("Autor: ")
            genre = input("Gênero: ")
            library.add_collection(Book(title, year, author, genre))
        
        elif choice == '2':
            title = input("Título da Revista: ")
            year = int(input("Ano: "))
            issue_number = input("Número da Edição: ")
            category = input("Categoria: ")
            library.add_collection(Magazine(title, year, issue_number, category))
        
        elif choice == '3':
            title = input("Título do DVD: ")
            year = int(input("Ano: "))
            director = input("Diretor: ")
            duration = int(input("Duração (em minutos): "))
            library.add_collection(DVD(title, year, director, duration))
        
        elif choice == '4':
            title = input("Título do CD: ")
            year = int(input("Ano: "))
            artist = input("Artista: ")
            track_count = int(input("Número de Faixas: "))
            library.add_collection(CD(title, year, artist, track_count))
        
        elif choice == '5':
            print("\n--- Coleções na Biblioteca ---")
            library.list_collections()
        
        elif choice == '6':
            print("Encerrando o sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

main()