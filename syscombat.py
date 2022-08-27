from sys import exit
from random import randint
from character import Char
from classeperson import ClasseHero
from mob import Monster
class Syscombat(Char,ClasseHero,Monster):
    def __init__(self,nick):
        Char.__init__(self,nick)
        ClasseHero.__init__(self)
        Monster.__init__(self)
        self.__RollDice = 0
        self.__Damage = 0
        self.__Defesa = 0
        self.__Hp = 50
     
    @property
    def rolldice(self):
        return self.__RollDice
    
    @rolldice.setter
    def rolldice(self,a,b='y'):
        if a != b:
            r = 'siga as instruções para completar a ação!'
            return r
        else:
            self.__RollDice = randint(1,7)
            return self.__RollDice
        
    @property
    def health(self):
        return self.__Hp

    @health.setter
    def health(self,a,b= 1):
        if a == b:
            self.__Hp += self.Forca*self.Vitalidade
            return self.__Hp
    
    @property
    def damage(self):
        return self.__Damage
    
    @damage.setter
    def damage(self,a,b = 1):
        if a == b:
            self.__Damage += (self.Forca + self.Agilidade) * self.Energia
            return self.__Damage
    
    @property
    def defesa(self):
        return self.__Defesa
    
    @defesa.setter
    def defesa(self,a,b = 1):
        if a == b:
            self.__Defesa += self.Forca / self.Agilidade
            return self.__Defesa


    def Ataque(self):
        self.HPmonster -= (self.__Damage - self.DefMonster)
        return (f'{self.nickname} bravamente consegue acerta-lo!\nDano Sofrido:{self.damage}\n{self.SkeletonWarrior}_Hp: {self.HPmonster}')
    def ataqueMob(self):
        self.__Hp -= (self.DmgMonster - self.__Defesa)
        return (f'{self.nickname} falhou em ataca-lo e foi supreendido com um ataque!\nDano Sofrido:{self.DmgMonster}\n{self.nickname}_Hp: {round(self.__Hp)}')
    def Died(self):
        return exit('Your Died')

    def Killmonster(self):
        self.nivel += 1
        return exit(f'{self.SkeletonWarrior} Died, ooooooohhh Level Up! Nivel:{self.nivel}')


        
        

    