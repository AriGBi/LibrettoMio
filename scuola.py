#COME ISTANZIARE UNA NUOVA CLASSE SU PYTHON:
class Person:
    def __init__(self,nome,cognome,eta,capelli,occhi,casa,incantesimo="Non ancora definito"): #costruttore della classe --> metodo init viene chiamato ogni volta che creo un'istanza della classe persona
       #per gli attributi che non si conoscono ancora, posso inizializzarlo nel costruttore="Non ancora definito"
       self.nome=nome  #il self sarebbe come il this.nome di java--> non posso omettere self
       self._cognome = cognome
       self.eta = eta
       self.capelli = capelli
       self.occhi = occhi
       self.casa = casa
       self.__prova = None
       self.incantesimo = incantesimo

    def __str__(self): #sarebbe il metodo toString()
        return f"{self.nome} - {self.cognome}"

    @property
    def cognome(self):  # eq. GETTER
       return self._cognome

    @cognome.setter
    def cognome(self, value):  # eq. SETTER
       # CONTROLLI per verificare che value sia compativile con _cognome
       self._cognome = value

    #pass -->si mette per non dare errore


class Student(Person): #classe Studente che eredita da Person
   def __init__(self,nome,cognome,eta,capelli,occhi,casa,animale,incantesimo="Non ancora definito",): #li devo mettere tutti e aggiungo quelli caratteristici solo di Student
      super().__init__(nome,cognome,eta,capelli,occhi,casa,incantesimo) #facendo cosi riprendo tutto ciò che c'era nell'__init__ di Person
      self.animale=animale

   def __str__(self): #faccio l'override perche voglio che stampi in modo diverso se è uno studente
      # ogni volta che stampo uno studente, uscirà così:
      return f"Studente:{self.nome} - {self.cognome} - {self.casa}" #stringa da far vedere al pubblico (piu carina)


   def __repr__(self):
      return f"Student(nome,cognome,eta,capelli,occhi,casa,animale" #print utile per il programmatore--> metto la stringa del costruttore cosi so come devo costruire l'oggetto

   def prettyPrint(self):
      print("Voglio stampare meglio")

   def copy(self):
      return Student(self.nome, self.cognome, self.eta, self.capelli, self.occhi, self.casa, self.animale, self.incantesimo)

class Teacher(Person):
   def __init__(self,nome,cognome,eta,capelli,occhi,casa,materia, incantesimo="Non ancora definito"):
      super().__init__(nome,cognome,eta,capelli,occhi,casa,incantesimo)
      self.materia=materia

   def __str__(self):
      # ogni volta che stampo un teacher uscirà così:
      return f"Teacher: {self.nome} - {self._cognome} - {self.materia} \n "


class Casa:
   def __init__(self, nome,studenti=[]): #quando costruisco una casa, creo immediatamente una lista VUOTA di studenti che poi ci metto dentro
      self.nome=nome #nome della casa
      self.studenti=studenti

   #per aggiungere studenti all'array:
   def addStudente(self,studente): #devo passare come parametro della funzione lo studente che voglio aggiungere
      self.studenti.append(studente) # --> aggiunge un solo elemento, quindi se passo una lista di studenti mi aggiunge LA LISTA in una sola casella
      #self.studenti.extend(studente) #se passo una lista di studenti, mi prende ogni singolo elemento e me lo aggiunge

   #se stampo una casa:
   def __str__(self):
      if len(self.studenti)==0:
         return f"La casa {self.nome} è vuota."

      myStr= f"\n Lista degli studenti iscrizzi alla casa {self.nome} \n"
      for s in self.studenti:
        myStr+=str(s) #sto DELEGANDO la stampa alla classe studenti, lo str(s) mi sta dicendo di usare il metodo __str__ di studente
          #dunque quando stampo una casa che ha degli studenti dentro, il modo in cui visualizzo gli studenti è quello definito nella classe Student
      return myStr


class Scuola:
   def __init__(self, case):
      self.case = case

   def __str__(self):
      mystr = ""
      for c in self.case:
         mystr += str(c) #di nuovo delego la stampa. Dicendo str(c), chiamo il metodo __str__ di c (che è un oggetto Casa)
      return mystr
