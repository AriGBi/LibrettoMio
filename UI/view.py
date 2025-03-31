import datetime

import flet as ft
#classe View deve conoscere il controller, quindi vorrei che ce lo avesse nel costruttore
class View:
    def __init__(self,page:ft.Page):
        self._txtOut = None
        self._btnCal = None
        self._ddVoto = None
        self._txtInNome = None
        self._student = None
        self._titolo = None
        self.txtOut = None
        self.btnIn = None
        self.txtIn = None
        self._controller = None
        self._page=page

    def loadInterface(self):
        """
        In questo metodo definiamo e carichiamo tutti i controlli dell'interfaccia
        :return:
        """
        self._titolo=ft.Text(value="Libretto Voti", color="red", size=24)
        self._student=ft.Text(value=self._controller.getStudent(),color="brown") #voglio visualizzare il nome dello studente, ma la view non lo conosce --> creo un metodo nel controller
        row1= ft.Row([self._titolo], alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._student],alignment=ft.MainAxisAlignment.END)

        self.txtIn= ft.TextField(label="Inserisci nome")
        self.btnIn=ft.ElevatedButton("Aggiungi", on_click=self._controller.handleAggiungi)

        #riga dei controlli
        self._txtInNome=ft.TextField(label="Nome esame", hint_text="Inserisci il nome dell'esame", width=300)
        self._ddVoto=ft.Dropdown(label="voto", width=120, )
        self._fillDDVoto() #chiamo il metodo fillDDVoto

        self._dp=ft.DatePicker( first_date=datetime.datetime(2022,1,1), last_date=datetime.datetime(2026,12,31) , on_change=lambda e: print(f"Giorno selezionato: {self._dp.value}"), on_dismiss=lambda e:print("Data non selezionata"))
        self._btnCal=ft.ElevatedButton(text="Pick date", icon=ft.Icons.CALENDAR_MONTH,on_click=lambda e: self._page.open(self._dp)) #date picker

        self._btnAdd=ft.ElevatedButton(text="Aggiungi", on_click=self._controller.handleAggiungi)
        self._btnPrint=ft.ElevatedButton(text="Stampa", on_click=self._controller.handleStampa)
        row3=ft.Row([self._txtInNome,self._ddVoto, self._btnCal, self._btnAdd, self._btnPrint], alignment=ft.MainAxisAlignment.CENTER)

        self._txtOut=ft.ListView(expand=True) #expad permette di scrollare

        #row=ft.Row(controls=[self.txtIn, self.btnIn])
        self._page.add(row1,row2,row3,self._txtOut)
        #self._page.add(self._titolo,row, self.txtOut) #l'ordine con cui aggiungo è l'ordine con cui visualizzo

    def setController(self,c): #nel main faccio conoscere il controller alla view
        self._controller = c

    def _fillDDVoto(self):
        for i in range(18,31):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))
