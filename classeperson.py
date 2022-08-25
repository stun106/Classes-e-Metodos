class ClasseHero:
    def __init__(self):
        self.__Blade_Knigth = {}
        self.__Soul_Master = {}
        self.__Muse_Elf = {}
        self.__Magic_Gladiator = {}
                                        
    #Métodos para seleção de personagens

    @property                               
    def HeroBK(self):
        return self.__Blade_Knigth
    
    @HeroBK.setter
    def HeroBK(self, a,b= 1 ):
        if a == b:
            self.__Blade_Knigth

    @property
    def HeroSM(self):
        return self.__Soul_Master

    @HeroSM.setter
    def HeroSM(self,a,b = 2):
        if a == b:
            return self.__Soul_Master

    @property
    def HeroME(self):
        return self.__Muse_Elf

    @HeroME.setter
    def HeroMe(self,a,b = 3):
        if a == b:
            return self.__Muse_Elf

    @property
    def HeroMG(self):
        return self.__Magic_Gladiator
    
    @HeroMG.setter
    def HeroMG(self,a,b = 4):
        if a == b:
            return self.__Magic_Gladiator


    
        
             




    
        