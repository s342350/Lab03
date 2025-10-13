import csv

from automobile import Automobile
from noleggio import Noleggio

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
    def __str__(self):
        return f"{self.nome}, {self.responsabile}, {self.codiceAutoCounter}, {self.codiceNoleggiCounter}"
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
        codice=f"A{self.codiceAutoCounter}"
        auto=Automobile(self.codiceAutoCounter,marca, modello, anno, num_posti)
        self.listaAuto.append(auto)
        self.codiceAutoCounter+=1
        return auto

        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def automobili_ordinate_per_marca(self):
        return sorted(self.listaAuto, key=lambda auto:auto.marca)
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        auto = None  # Inizializziamo la variabile auto a None, cioè "non trovata"
        for a in self.listaAuto:  # Per ogni automobile nella lista
            if a.codice == id_automobile:  # Se il codice corrisponde a quello cercato
                auto = a  # si assegna l'auto trovata alla variabile auto
                break  # Uscimo dal ciclo, non serve cercare oltre

        if auto is None:
            print("Errore: automobile non trovata.")
            return None

        for n in self.noleggiAttivi:
            if n.id_automobile == id_automobile:
                print("Errore: automobile già noleggiata.")
                return None

        codice_noleggio = f"N{self.codiceNoleggiCounter}"
        noleggio = Noleggio(codice_noleggio, data, id_automobile, cognome_cliente)

        self.noleggiAttivi.append(noleggio)
        self.codiceNoleggiCounter += 1

        return noleggio

        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        for n in self.noleggiAttivi:
            if n.codice == id_noleggio:
                self.noleggiAttivi.remove(n)
                print(f"Noleggio {id_noleggio} terminato.")
                return True
        print("Errore: noleggio non trovato.")
        return False
        """Termina un noleggio in atto"""
        # TODO
