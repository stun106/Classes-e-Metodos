class Char:
    def __init__(self,nick):
        self.id = 'stun106'
        self.nickname = nick
        self. __inventario = {}

    @property
    def inventario(self)->dict:
        return self.__inventario

    @inventario.setter
    def inventario(self,a:bool,b='i',info = 'Hotkey incorreta, siga as instruções a cima!'):
        if a == b:
           return self.__inventario
        else:
            return info