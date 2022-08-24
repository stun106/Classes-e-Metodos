class Char():
    def __init__(self,nick):
        self.id = 'stun106'
        self.nickname = nick
        self.__exp = 0
        self.nivel = 1
        self. __inventario = {}

    @property
    def inventario(self)->dict:
        return self.__inventario

    @inventario.setter
    def inventario(self,a,b='i',info = 'Hotkey incorreta, siga as instruções a cima!'):
        if a == b:
           return self.__inventario
        else:
            return info

    @property
    def upExp(self):
        return self.__exp

    @upExp.setter
    def upExp(self,a:str):
        if self.__exp == 100:
            self.nivel +=1
            a = 'Level Up!'
            return (f'{a} Level: {self.nivel}')
        else:
            return self.__exp


    def addInventario(self,a:str,b:int)->dict:
        self.__inventario[a] = b
        return self.__inventario



