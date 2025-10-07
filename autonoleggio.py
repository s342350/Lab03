import csv

from automobile import Automobile

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self.nome=nome
        self.responsabile=responsabile
        self.listaAuto=[]
        self.noleggiAttivi=[]
        self.codiceAutoCounter=1
        self.codiceNoleggiCounter=1

        """Inizializza gli attributi e le strutture dati"""
        # TODO

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                reader=csv.reader(f)
                for row in reader:
                    codice, marca, modello, anno, n_posti=row
                    auto = Automobile(codice, marca, modello, anno, n_posti)
                    self.listaAuto.append(auto)
        except FileNotFoundError:
            print("errore nella lettura del file")

        # TODO

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        auto=Automobile(self.codiceAutoCounter,marca, modello, anno, num_posti)
        self.listaAuto[self.codiceAutoCounter]=auto
        self.codiceAutoCounter+=1

        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def automobili_ordinate_per_marca(self):
        return sorted(self.listaAuto, key=lambda auto:auto.marca)
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
