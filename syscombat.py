from random import randint
from statushero import status
class Syscombat:
    def __init__(self):
        self.atributos = status()
        self.__RollDice = 0
        self.__Damage = 0
        self.__Defesa = 0
        self.__HP = 50
     
    @property
    def rolldice(self):
        return self.__RollDice
    
    @rolldice.setter
    def rolldice(self,a,r):
        if a == 'y':
            r = 'siga as instruções para completar a ação!'
            return r
        else:
            self.__RollDice = randint(1,7)
            return self.__RollDice
        
    @property
    def health(self):
        return self.__HP

    @health.setter
    def health(self,a='You Died!'):
        if self.__HP <= 0:
            return a
        else: 
            self.__HP += self.atributos.Forca * self.atributos.Vitalidade
            return self.__HP
    
    @property
    def PvM(self):
        return self.__Damage

    @PvM.setter
    def PvM(self,a, b = 'ataque'):
        if a == b:
            while True:
                if self.__RollDice <= 4: 
                    self.__Damage += (self.atributos.Forca + self.atributos.Agilidade)/self.atributos.Energia
                    #continua...

    


        
    
    