#contiene solo una classe che si chiama Controller
#nel controller vanno le funzioni di handle!!
from view import View
from voto.voto import Libretto, Voto
from scuola import Student
import flet as ft

class Controller:
    def __init__(self,v:View):
        self._view=v
        self._student=Student("Harry","Potter", 11,"castani","castani","Grifondoro","civetta", "Expecto Patronum")
        self._model=Libretto(self._student,[]) #la classe libretto l'ho chiamata model
        self._fillLibretto() #riempio il libretto


    def handleAggiungi(self,e):
        # strIn=self._view.txtIn.value #leggo la stringa del txt in ingresso
        # if strIn=="":
        #     self._view.txtOut.value="Errore: campo vuoto"
        #     self._view._page.update()
        #     return
        # else:
        #     self._view.txtOut.value=strIn  #salvo in txtOut il valore della stringa txtIn
        #     self._view._page.update()

        """
        raccoglie tutte le info per creare un nuovo voto, lo crea e lo aggiunge al libretto
        :param e:
        :return:
        """
        nome=self._view._txtInNome.value
        if nome=="":
            self._view._txtOut.controls.append(ft.Text("Attenzione il campo nome non può essere vuoto", color = "red"))
            self._view._page.update()
            return
        punti= self._view._ddVoto.value
        if punti is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione selezionare un voto", color="red"))
            self._view._page.update()
            return
        data= self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione inserire la data", color="red"))
            self._view._page.update()
            return
        if punti=="30L":
            self._model.append(Voto(nome,30,f"{data.year}-{data.month}-{data.date}",True))
        else:
            self._model.append(Voto(nome, punti, f"{data.year}-{data.month}-{data.date}", False))
        self._view._txtOut.controls.append(ft.Text("Voto correttamente aggiunto", color="green"))
        self._view._page.update()




    def handleStampa(self,e):
        self._view._txtOut.controls.append(ft.Text(str(self._model)))
        self._view._page.update()



    def getStudent(self):
        """
        restituisce informazioni dello studente, usando il __str__ dell'oggetto student
        :return:
        """
        #per prendere lo studente, lo devo prendere dal modello e quindi importare il modello come attributo
        return str(self._student)

    def _fillLibretto(self): #si mettte il il trattino davanti per dire che questo metodo viene usato solo in questa classe
        v1 = Voto("Difesa contro le arti oscure", 30, "2022-01-03", True)
        v2 = Voto("Babbanologia", 22, "2022-02-12", False)
        self._model.append(v1)
        self._model.append(v2)
        self._model.append(Voto("Pozioni", 22, "2022-06-14", False))
