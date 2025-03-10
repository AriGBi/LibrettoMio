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

print("\nVerifico metodo hasVoto:")
print(mylib.hasVoto(v1))
print(mylib.hasVoto(Voto("Aritmanzia",30,"2023-07-10",False)))
print(mylib.hasVoto(Voto("Difesa contro le arti oscure", 30, "2022-01-03",True)))

print("\nVerifico metodo hasConflitto:")
print(mylib.hasConflitto(Voto("Difesa contro le arti oscure", 21, "2022-01-03",False)))


print("\nTest append modificata")
mylib.append(Voto("Aritmanzia",30,"2023-07-10",False)) #aggiungo un voto non presente nel libretto
#mylib.append(Voto("Difesa contro le arti oscure", 21, "2022-01-03",False)) #aggiungo un voto presente nel libretto

mylib.append(Voto("Divinazione",27,"2021-02-08",False))
mylib.append(Voto("Cura delle creature magiche", 26,"2021-02-08",False ))
print("------------------------------------------")
print("Libretto originario")
print(mylib)

nuovoLib =mylib.creaMigliorato()
print("-------------------------------------------")
print("Nuovo libretto migliorato")
print(nuovoLib)



