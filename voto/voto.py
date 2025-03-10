import operator
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

@dataclass(order=True) #devo usare decoratore dataclass prima della classe successiva per indicare che è una dataclass
#la dataclass permette di contenere i metodi minimi utili per una classe senza dover scrivere troppe rige
#si deve indicare il TIPO di variabile anche se Python è un linguaggio non tipizzato, si fa solo per capire se si sta sagliando qualcosa

#mettendo @dataclass(eq =False) sto dicendo di implementare tutti i metodi minimi tranne __eq__
#mettendo @dataclass(order=True) dico che la classe Voto è ordinabile
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

    def __hash__(self):
        return hash((self.materia, self.punteggio,self.lode))

class Libretto:
   def __init__(self, proprietario, voti=[]):
      self.proprietario = proprietario
      self.voti = voti #list di OGGETTI voti

   def append(self, voto): # duck!
       if(self.hasConflitto(voto) is False and self.hasVoto(voto) is False):
          self.voti.append(voto)

       else:
           raise ValueError("Il voto è gia presente")

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

   #FUNZIONI FIND--> get di alcuni elementi che hanno determinate caratteristiche
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

       # voglio un metodo che controlli se un voto c'è già o meno nel libretto --> voglio che restituisca un booleano quindi la chiamo "has--"

   def hasVoto(self, voto):
       """
       verifica se il libretto contiene già il voto "voto". Due voti sono ritenuti uguali se hanno lo stesso campo materia e lo stesso campo punteggio
       (voto è formato da due campi: punteggio e lode)
       :param voto: istanza dell'oggetto di tipo voto
       :param lode: booleano che indica se presente la lode
       :return: True se il voto è gia presente, False altrimenti
       """
       for v in self.voti:
           # modo numero 1:
           if v == voto:
               pass
           # modo numero 2:
           if v.punteggio == voto.punteggio and v.materia == voto.materia and v.lode == voto.lode:
               return True
       return False

   def hasConflitto(self, voto):
       """
       Questo metodo controlla che il voto "voto" non rappresenti un conflitto con i voti già presenti nel libretto.
       Consideriamo due voti in conflitto quando hanno lo stesso campo materia ma diversa coppia (punteggio,lode)
       :param voto: istanza della classe Voto
       :return: True se voto è in conflitto, False altrimenti
       """

       for v in self.voti:
           if(v.materia == voto.materia and not(v.punteggio==voto.punteggio and v.lode == voto.lode) ):
               return True
       return False

   #metodo di FACTORING --> creo un nuovo libretto
   def copy(self):
       """
       crea una nuova copia del libretto
       :return: istanza della classe libretto
       """
       nuovo = Libretto(self.proprietario,[]) # in nuovo creo una NUOVA ISTANZA VOTO con gli stessi attributi del vecchio libretto,
           #così quando modifico nuovo non va a modificarmi anche il libretto originale
       for v in self.voti:
           nuovo.append(v.copy()) #aggiunge sul nuovo libretto una copia dei voti
        #DEEP COPY --> creo una copia del libretto che contiene una copia dei voti
       return nuovo

   def creaMigliorato(self):
       """
       Crea un nuovo oggetto libretto in cui i voti sono migliorati secondo la seguente logica:
       se il voto è >=18 e <24 , aggiungo +1
       se il voto è >= 24 e <29 aggiungo +2
       se il voto è 29 aggiungo +1
       se il voto è 30 rimane 30
       :return: nuovo libretto
       """
       nuovo = self.copy() #creo effettivamente la COPIA dell'oggetto libretto che sto trattando ora

        # modifico i voti in nuovo
       for v in nuovo.voti:
           if 18<=v.punteggio<24:
               v.punteggio+=1
           elif 24<=v.punteggio<29:
               v.punteggio+=2
           elif v.punteggio==29:
               v.punteggio = 30

       return nuovo

   def sortByMateria(self): #metodo agisce sul libretto e ordina la lista contenente nel libretto
       #self.voti.sort(key= estraiMateria) --> Opzione in cui creo un metodo estraiMateria in cui prendo voto.materia
       self.voti.sort(key=operator.attrgetter("materia")) #equivale a fare voto.materia

   def cancellaInferiori(self, punteggio):
       """
       Questo metodo agisce sul libretto corrente eliminando ruttu i voti inferiori al parametro punteggio
       :param punteggio: intero indicante il valore minimo del punteggio accettato
       :return:
       """
       #modo 1:
       # for i in range(len(self.voti)):
       #     if self.voti[i].punteggio < punteggio:
       #         self.voti.pop(i)
       #T=0 -- [18 18 18 26 27 28] i=0
       #T=1 -- [18 18 26 27 28] i=1
       #T=2 -- [18 26 27 28] i=2
       # ora controlla il 26 perchè è in posizione 2, ma è >24 e quindi non succede niente
       #out -- [18 26 27 28] --> non va bene perchè non mi ha eliminato il 18

       #modo 2:
       # for v in self.voti:
       #     if v.punteggio < punteggio:
       #         self.voti.remove(v)

       #modo 3:
       nuovo=[]
       for v in self.voti:
            if v.punteggio >= punteggio:
               nuovo.append(v) #sto riutilizzando gli oggetti che ho, non ne sto creando di nuovi
       self.voti=nuovo #modifico i voti del libretto attuale




   #def sortByVoto(self):


    # Opzione 1: creo due metodi di stampa, che prima ordinano e poi stampano --> non va bene perchè mischio sorting e print
    # Opzione 2: creo due metodi che ordinano la lista di self e poi un'unico metodo di stampa --> non va bene perchè modificherei la lista
    # Opzione 3: creo due metodi che si fanno la copia della lista, la ordinano e la restituiscono. Poi un altro metodo si occuperà di stampare le niuove liste --> opzione più versatile perchè lavoro su delle copie
    # Opzione 4: creo una shallow copy (copio solo la lista e gli oggetti dentro rimangono quelli vecchi--> agisco solo sulla lista e non sugli oggetti) di self.voti e ordino quella

   # implemento Opzione2:
   def creaLibOrdiantoPerVoto(self):
       nuovo = self.copy()
       #nuovo.sort(key=operator.attrgetter("punteggio")) #non funziona bene perchè noi abbiamo anche il campo lode, serve una funzione che
       nuovo.voti.sort(key=lambda v: (v.punteggio,v.lode), reverse =True) #ordina prima per il primo campo della tupla e poi per il secondo (Python sa ordinare le tuple)
       # reverse è un parametro della funzione sort che lo fa al contrario
       return nuovo

   #implemento Opzione 3:
   def creaLibOrdinatoPerMateria(self):
       """
       Crea un nuovo oggetto libretto e lo ordina per materia
       :return: nuova istanza dell'oggetto libretto
       """
       nuovo = self.copy()
       nuovo.sortByMateria()

       return nuovo
def estraiMateria(voto):
    """
    Questa materia restituisce il campo materia dell'oggetto voto
    :param voto: istanza della classe Voto
    :return: stringa rappresentante il nome della materia
    """
    return voto.materia

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
