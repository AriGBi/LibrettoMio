from voto.voto import Voto,Libretto

#faccio un file a parte per testare un modulo (volendo posso farlo direttamente all'interno del modulo --> ma il modulo non dovrebbe teoricamente contenere nulla che sia eseguibile)
v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
v2 = Voto("Pozioni", 30, "2022-02-17", True)
v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
print(v1)
