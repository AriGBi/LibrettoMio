from dataclasses import dataclass


@dataclass
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    # def __eq__(self,other):
    #     return(self.punteggio == other.punteggio and self.lode == other.lode and self.materia == other.materia)
    # non va bene perchè sto specializzando troppo il metodo eq che magari voglio usare diversamente in futuro

    def copy(self): #è un metodo che crea un NUOVO VOTO (con nuovo riferimento) ma con gli stessi attributi del voto corrente
        # è un metodo FACTORING --> metodo della classe che crea un nuovo oggetto della classe.
        return Voto(self.materia, self.punteggio, self.data, self.lode)

    def __eq__(self,other):
        return self.materia == other.materia #dico che 2 oggetti voti sono uguali se hanno la stessa materia

    def __hash__(self):
        return hash(self.materia) #IDENTIFICO un oggetto in base alla sua materia
