from dataclasses import dataclass
import math
import flet
# class Voto:
#     def __init__(self, materia, punteggio, data, lode):
#         if  punteggio == 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = lode
#         elif punteggio < 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = False
#         else:
#             raise ValueError(f"Attenzione, non posso creare un voto con punteggio {punteggio}")
#     def __str__(self):
#         if self.lode:
#             return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
#         else:
#             return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

@dataclass #devo usare decoratore dataclass prima della classe successiva per indicare che è una dataclass
#la dataclass permette di contenere i metodi minimi utili per una classe senza dover scrivere troppe rige
#si deve indicare il TIPO di variabile anche se Python è un linguaggio non tipizzato, si fa solo per capire se si sta sagliando qualcosa
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


class Libretto:
   def __init__(self, proprietario, voti=[]):
      self.proprietario = proprietario
      self.voti = voti #list di OGGETTI voti

   def append(self, voto):  # duck!
      self.voti.append(voto)

   def __str__(self):
      mystr = f"Libretto voti di {self.proprietario} \n"
      for v in self.voti:
         mystr += f"{v} \n"
      return mystr

   def __len__(self):
      return len(self.voti)

   def calcolaMedia(self):
       #per tutti i metodi devo scrivere un commento come il seguente in cui dico cosa fa il metodo e cosa ritorna,
       #in questo modo se ci schiaccio sopra sul main posso vedere cosa ho scritto
       """
       restituisce la media dei voti attualmente presenti nel libretto
       :return: valore numerico della media, oppure ValueError in caso di lista vuota
       """

       #media= somma_voti/num_esami
       numEsami=len(self.voti)
       if len(self.voti)==0:
           raise ValueError("Attenzione lista esami vuota.")

       v=[v1.punteggio for v1 in self.voti] #equivale a dire voti=[] e poi for v1 in self.voti: v.append(v1.punteggio)
       return sum(v)/numEsami #posso anche fare math.mean(v) e ottengo la media dei voti oresenti nella lista v

   def getVotiByPunti(self,punti,lode): #Voti plurale perchè potrebbero essere piu di uno
       """
       restituisce una lista di esami con punteggio uguale a punti (e lode se applicata)
       :param punti: variabile di tipo intero che rappresenta il punteggio
       :param lode: booleano che indica se presente la lode
       :return: lista di voti
       """
       votiFiltrati=[]
       for v in self.voti:
           if v.punteggio == punti and v.lode == lode:
               votiFiltrati.append(v)
       return votiFiltrati

   def getVotobyName(self,nome): #Voto singolare così so che è uno sono
       """
       restituisce un oggetto Voto il cui campo materia è uguale al parametro nome che passo
       :param nome: stringa che indica il nome della materia 
       :return: oggetto di tipo Voto oppure None in caso di voto non trovato
       """
       for v in self.voti:
            if v.materia == nome:
                return v

def testVoto():
        v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
        v2 = Voto("Pozioni", 30, "2022-02-17", True)
        v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
        print(v1) # controllo che i voti funzionino
        mylib = Libretto("Harry", [v1, v2])
        print(mylib)
        mylib.append(v3) # append è una funzione che ho definito nella classe Libretto
        print(mylib) #controllo che i libretti funzionino
        print(math.cos(3.14))
        print(flet.Text(mylib))

if __name__ == "__main__": #uso questo costrutto per dire "se sto runnando questo modulo DA SOLO (ovvero __name__= "__main__") esegui le seguenti istruzioni"
        # __name__ sarà uguale a voto SE sono in un'altra classe e ho importato voto e lo sto runnando --> in quel caso non voglio che le seguenti istruzioni vengano eseguite
        # in particolare sono istruzioni di TEST --> voglio eseguirle solo se sto testando la singola classe, non voglio eseguirle quando sto USANDO la classe nel main
        testVoto() #runno il test
