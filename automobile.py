class Automobile:
    def __init__(self, codice, marca, modello, anno, n_posti):
        self.codice=codice
        self.marca=marca
        self.modello=modello
        self.anno=anno
        self.n_posti=n_posti

    def __str__(self):
        return f"{self.codice}: {self.marca}, {self.modello}, {self.anno}, {self.n_posti}"
