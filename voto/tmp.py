class Prova:
    _myClassVariable = 0 #attributo a cui ho accesso senza fare self. perchè è fuori dal costruttore
    def __init__(self):
        myIstanceVariable=1
        pass

    def standardMethod(self,input): #in queste classi ho accesso a self
        self.myInstanceVariable=input


    @staticmethod
    def staticMethod(): #qui non ho accesso ne a self ne agli attributi
        pass

    @classmethod
    def classMethod(cls): #qui non ho accesso a self, ma ho accesso agli attributi fuori dal costruttore
        print(cls._myClassVariable)
