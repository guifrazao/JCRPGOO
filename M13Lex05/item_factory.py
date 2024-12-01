from book import Book
from magazine import Magazine
from dvd import DVD
from cd import CD

class ItemFactory:
    @staticmethod
    def create_item(item_type, *args):
        if item_type == "Livro":
            return Book(*args)
        elif item_type == "Revista":
            return Magazine(*args)
        elif item_type == "DVD":
            return DVD(*args)
        elif item_type == "CD":
            return CD(*args)
        else:
            raise ValueError("Tipo de item desconhecido.")
