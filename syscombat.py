from random import randint
from character import Char
from statushero import status
from mob import Monster
class Syscombat(Char,status,Monster):
    def __init__(self):
        self.Mob = Monster()
        self.__RollDice = 0
        self.__Damage = 0
        self.__Defesa = 0
        self.__Hp = 50
     
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
        return self.__Hp

    @health.setter
    def health(self,a='You Died!'):
        if self.__HP <= 0:
            return a
        else: 
            self.__HP += self.Forca * self.Vitalidade
            return self.__Hp
    
    @property
    def damage(self):
        return self.__Damage
    
    @damage.setter
    def damage(self):
        if self.__Damage > 1:
            self.__Damage += (self.Forca + self.Agilidade) / self.Energia
            return self.__Damage
    
    @property
    def defesa(self):
        return self.__Defesa
    
    @defesa.setter
    def defesa(self):
        if self.__Defesa > 1:
            self.__Defesa += self.Forca / self.Agilidade
            return self.__Defesa

    def PvM(self,a, b = 'ataque'):
        if a == b:
            while True:
                if self.__RollDice <= 4: 
                    self.HPmonster -= (self.__Damage - self.DefMonster)
                    return self.HPmonster
                elif self.__Hp == 0:
                    r = 'Your Died'
                    return r
                elif self.HPmonster == 0:
                    self.nivel += 1
                    r = (f'{self.SkeletonWarrior} Died, ooooooohhh Level Up! Nivel:{self.nivel}')
                    self.__inventario['ouro'] = 500
                    o = '500 ouro adquirido'
                    return (r,o)
                else: 
                    self.__Hp -= (self.Mob.DmgMonster - self.__Defesa)
                    return self.__Hp


                    

    


        
    
    