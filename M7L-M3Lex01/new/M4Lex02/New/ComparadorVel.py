class VelocidadeComparator:
    def comparar(self, bike1, bike2):
        return abs(bike1.get_velocidade() - bike2.get_velocidade())