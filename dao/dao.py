import mysql.connector

from dao.DBConnect import DBConnect
from voto.voto import Voto


class LibrettoDAO:
    def __init__(self):
        self.dbConnect=DBConnect()

    @staticmethod #mi dice che non sono metodi che si riferiscono a un'istanza della classe --> tolgo il self dai parametri
    def getAllVoti():
        """
        Chiede al server di avere tutti i voti nel datase
        """
        cnx=DBConnect.getConnection()
        cursor=cnx.cursor(dictionary=True) #oggetto iterabile nel quale per ogni riga avremo una riga della tabella

        query="""select * from voti"""
        cursor.execute(query)
        res=[]
        for row in cursor: #ogni row è la riga nella tabella --> row: {data: " ", lode: " ", materia: " ", punteggio: " "}
            materia=row["materia"]
            data=row["data"] #è un oggetto dateTime (lo converte il cursore in dateTime)
            punteggio=row["punteggio"]
            lode=row["lode"]
            if lode=="False":
                res.append(Voto(materia,punteggio, data.date(),False))
            else:
                res.append(Voto(materia,punteggio, data.date(), True))
            #si poteva fare --> res.append(Voto(row["materia],row["punteggio"],row["data],row["lode"]
            print(row)

        cnx.close()
        return res

    @staticmethod
    def addVoto(voto: Voto):
        cnx=DBConnect.getConnection()
        cursor=cnx.cursor(dictionary=True)
        query="insert into voti (materia,punteggio,data,lode) values (%s,%s,%s,%s)" #template query
        cursor.execute(query, (voto.materia,voto.punteggio,voto.data,voto.lode))
        cnx.commit()
        cnx.close()
        return

    @staticmethod
    def hasVoto(self,voto:Voto):
        cnx=DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)
        query="""select * from voti v where v.materia=%s"""
        cursor.execute(query, (voto.materia,))
        res=cursor.fetchall() #leggo i dati trovati --> res sarà una lista di righe che ha o un elemento o nessuno (in base a se la materia c'era o no)
        cnx.close()
        return len(res)>0



if __name__ == "__main__":
    mydao=LibrettoDAO()
    mydao.getAllVoti()
