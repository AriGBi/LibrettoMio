from scuola import Student
from voto.voto import Libretto, Voto

Harry=Student("Harry","Potter", 11,"castani","castani","Grifondoro","civetta", "Expecto Patronum")
mylib=Libretto(Harry,[])
v1=Voto("Difesa contro le arti oscure", 30, "2022-01-03",True)
v2=Voto("Bavvanologia",22, "2022-02-12",False)
mylib.append(v1)
mylib.append(v2)
mylib.append(Voto("Pozioni",22,"2022-06-14",False))
mylib.calcolaMedia()

votiFiltrati=mylib.getVotiByPunti(30,True)
print(votiFiltrati)

votoPozioni=mylib.getVotobyName("Pozioni")
if votoPozioni is None:
    print("Voto non trovato")
else:
    print(votoPozioni.materia)
