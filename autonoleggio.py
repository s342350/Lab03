import csv
from automobile import Automobile
class Autonoleggio:
    def __init__(self, nome, responsabile):
        self.nome=nome
        self.responsabile=responsabile
        self.id_attributi={}

        """Inizializza gli attributi e le strutture dati"""
        # TODO

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        listaDiAuto=[]
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                reader=csv.reader(f)
                for row in reader:
                    marca, modello, anno, n_posti=row
                    listaDiAuto.append(row)

        except FileNotFoundError:
            print("errore nella lettura del file")
        return listaDiAuto
        # TODO

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        self.marca=marca
        self.modello=modello
        self.anno=anno
        self.num_posti=num_posti
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def automobili_ordinate_per_marca(self):
        #return sorted(self., key =lambda a:a.marca)
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
