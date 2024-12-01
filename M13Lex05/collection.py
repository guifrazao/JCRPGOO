from abc import ABC, abstractmethod

# Classe abstrata Collection
class Collection(ABC):  
    """
    Classe abstrata que serve como base para todos os tipos de acervo.
    Define a estrutura comum para os acervos e garante que as subclasses implementem o método 'get_details'.
    """
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @abstractmethod
    def get_details(self):  
        """
        Método abstrato que deve ser implementado pelas subclasses.
        Obriga as subclasses a fornecerem uma descrição detalhada do item.
        """
        pass
