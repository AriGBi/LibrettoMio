import pathlib

import mysql.connector


class DBConnect:
    def __init__(self):
        RuntimeError("Non creare un'istanza di questa classe") #impedisco di creare un OGGETTO DBConnect

    _myPool=None
    # @classmethod
    # def getConnection(cls): --> questo metodo non va piu bene se vogliamo fare il pooling
    #     try:
    #         cnx = mysql.connector.connect(
    #             user="root",
    #             password="rootroot",
    #             host="localhost",
    #             database="libretto"
    #         )
    #         return cnx
    #     except mysql.connector.Error as err:
    #         print("Non riesco a collegarmi al database")
    #         print(err)

    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            try:
                #creo una connessione e restituisco il metodo get_connection
                cls._myPool=mysql.connector.pooling.MySQLConnectionPool(
                    option_files=f"{pathlib.Path(__file__).resolve().parent}/connection.cfg",

                    pool_size=3,
                    pool_name="myPool"
                )
            except mysql.connector.Error as err:
                print("Something is wrong in dbConnect")
                print(err)
                return None
            return cls._myPool.get_connection()
        else:
            #se il pool già esiste, restituisco la connessione
            return cls._myPool.get_connection()
