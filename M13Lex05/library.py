from collection import Collection

class Library:
    def __init__(self):
        self.collections = []

    def add_collection(self, collection):
        if isinstance(collection, Collection):
            self.collections.append(collection)
        else:
            print("O item deve ser uma coleção válida.")

    def list_collections(self):
        for item in self.collections:
            print(item.get_info())