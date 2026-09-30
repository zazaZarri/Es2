from libro import Libro

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def conta_libri(self):
        return len(self.libri)

    def cerca_per_titolo(self, titolo):
        risultati = []
        for libro in self.libri:
            if titolo.lower() in libro.titolo.lower():
                risultati.append(libro)
        return risultati

    def cerca_per_autore(self, autore):
        risultati = []
        for libro in self.libri:
            if autore.lower() in libro.autore.lower():
                risultati.append(libro)
        return risultati