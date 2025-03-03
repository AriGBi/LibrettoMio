import math #crea un namespace SEPARATO e mi riporta tutti i nomi presenti in math, tenendoli separati dai miei
# posso rinominare i moduli --> import math as m
# con import, se faccio il debug vedo che mi importa math come una funzione esterna
x=3.14
print(math.sin(x))

from math import cos # prendo il nome cos da math e lo aggiungo al mio modulo,
                    # diventa equivalente a tutto ciò che ho nel mio modello --> si mischiano i nomi mieni (i miei oggetti) con i nomi di math
# la notazione from importa nomi singoli, che finiscono nel namespace del mio modulo (non uso la notazione puntata per accedervi, ma semplicemente il nome)
# inoltre se faccio il debug, vedo che cos viene messo nell'elenco delle cose create da ME (non in Special Variables), come se fosse una funzione che ho creato io nel file

# con from math import * --> prende tutti i nomu di math e li mette del mio namespace (pericoloso perchè ci possono essere conflitti tra nomi locali e nomi di math)

x=3.14
# se voglio sapere tutte le cose che ci sono nel namespace, uso nella console la parola dir()

print(math.sin(x))
print(cos(x))
print("ciao")

# se faccio debug e poi Console --> posso scrivere dir() e vedere tutte le variabili che ci sono nel mio namespace.
#In questo caso usciranno 'x', 'math', 'cos'
