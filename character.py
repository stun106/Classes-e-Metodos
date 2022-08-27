class Char():
    def __init__(self,nick):
        self.nickname = nick
        self.nivel = 1
        self.__inventario = {}
    
    @property
    def inventario(self)->dict:
        return self.__inventario

    @inventario.setter
    def inventario(self):
        if self.inventario == dict :
           return self.__inventario

    def addInventario(self,a:str,b:int)->dict:
        self.__inventario[a] = b
        return self.__inventario



