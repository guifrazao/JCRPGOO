from library import Library


# Criar uma instância da biblioteca
library = Library()

library.add_book("1984", "George Orwell", 1)
library.add_book("Dom Casmurro", "Machado de Assis", 2)

library.display_books()

library.borrow_book("1984", "João")

library.display_books()

library.borrow_book("1984" , "Gustavo")

library.return_book("1984", "João")

library.display_books()

library.borrow_book("1984" , "Gustavo")