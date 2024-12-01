from mouse import Mouse
from book import Book

def main():
    # Criando produtos (mouses e livros)
    mouse1 = Mouse("Mouse USB", 100.0, "Mouse ótico, Saída USB. 1.600 dpi", "Óptico")
    mouse2 = Mouse("Mouse Bluetooth", 150.0, "Mouse sem fio, Bluetooth 5.0", "Bluetooth")
    book1 = Book("Python para Iniciantes", 50.0, "Aprenda Python do básico ao avançado", "Carlos Silva")
    book2 = Book("O Poder do Hábito", 40.0, "Entenda como os hábitos afetam sua vida", "Charles Duhigg")

    # Simulando o carrinho de compras com os produtos
    cart = [mouse1, mouse2, book1, book2]

    # Exibindo as descrições dos produtos no carrinho
    for product in cart:
        print(product.get_description())

main()
