class ClasseHero:
    def __init__(self):
        self.Blade_Knigth = {}
        self.Soul_Master = {}
        self.Muse_Elf = {}
        self.Magic_Gladiator = {}
                                        
    #Métodos para seleção de personagens

    # @property                               
    def selectHero(self,a,b = 1,c = 2,d = 3,e = 4 ):
        if a == b:
            x ='você escolheu o Guerreiro Blade Knigth'
            return (f'{x}:{self.Blade_Knigth}')
        elif a == c:
            x = 'você escolheu o Mago Soul Master'
            return (f'{x}:{self.Soul_Master}')
        elif a == d:
            x = 'você escolheu a Arqueira elemental Muse Elf:'
            return (f'{x}:{self.Muse_Elf}')
        else:
            if a == e: 
                x = 'você escolheu o Magico Gladiador'
            return (f'{x}:{self.Magic_Gladiator}')
    
    # # @HeroBK.setter
    # # def HeroBK(self, a,b= 1 ):
    # #     if a == b:
    # #         self.__Blade_Knigth

    # # @property
    # def HeroSM(self):
    #     return self.Soul_Master

    # # @HeroSM.setter
    # # def HeroSM(self,a,b = 2):
    # #     if a == b:
    # #         return self.__Soul_Master

    # # @property
    # def HeroME(self):
    #     return self.Muse_Elf

    # # @HeroME.setter
    # # def HeroMe(self,a,b = 3):
    # #     if a == b:
    # #         return self.__Muse_Elf

    # # @property
    # def HeroMG(self):
    #     return self.Magic_Gladiator
    
    # # @HeroMG.setter
    # # def HeroMG(self,a,b = 4):
    # #     if a == b:
    # #         return self.__Magic_Gladiator


    
        
             




    
        