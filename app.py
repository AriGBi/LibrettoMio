# questo file in realtà di solito si chiama main, ma abbiamo gia un file chiamato main
import flet as ft

from controller import Controller
from view import View


def main(page: ft.Page):
    #creo istanze di View e Controller e voglio che si conoscano a vicenda
    v=View(page) #la classe view deve conoscere anche la pagina perchè la sto creando in un'altra classe(app/main)
    c=Controller(v) #posso passare al controller come parametro la view
    v.setController(c) #creo un metodo dentro view per far si che la view conosca il controller
    v.loadInterface() #devo chiamarlo dopo aver settato il controller perchè gli serve conoscerlo



ft.app(target=main)
