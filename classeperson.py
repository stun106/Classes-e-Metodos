class ClasseHero:
    def __init__(self):
        self.__Blade_Knigth = {}
        self.__Soul_Master = {}
        self.__Muse_Elf = {}
        self.__Magic_Gladiator = {}
        self.Forca = 0
        self.Agilidade = 0
        self.Vitalidade = 0
        self.Energia = 0
                             
    #Métodos para seleção de personagens

    @property                               
    def selectBK(self):
        x ='você escolheu o Guerreiro Blade Knigth'
        return (f'{x}:{self.__Blade_Knigth}')
    
    @selectBK.setter
    def selectBK(self, a,b= 1 ):
         if a == b:
            return self.__Blade_Knigth

    @property
    def selectSM(self):
        x = 'você escolheu o Mago Soul Master'
        return (f'{x}:{self.__Soul_Master}')

    @selectSM.setter
    def selectSM(self,a,b = 2):
         if a == b:
            
            return self.__Soul_Master

    @property
    def selectME(self):
        x = 'você escolheu a Arqueira elemental Muse Elf:'
        return (f'{x}:{self.__Muse_Elf}')

    @selectME.setter
    def selectMe(self,a,b = 3):
         if a == b:
            
            return self.__Muse_Elf

    @property
    def selectMG(self):
        x = 'você escolheu o Magico Gladiador'
        return (f'{x}:{self.__Magic_Gladiator}')
    
    @selectMG.setter
    def selectMG(self,a,b = 4):
         if a == b:
            
            return self.__Magic_Gladiator


    #Métodos para atribuir status do personagem

    def BkStatus(self,a,b = 1): 
        if a == b:
            self.selectBK = a
            self.Forca += 10
            self.__Blade_Knigth['Str'] = 10 
            self.Agilidade += 4
            self.__Blade_Knigth['Agi'] = 4
            self.Vitalidade += 3
            self.__Blade_Knigth['Vit'] = 3
            self.Energia += 3
            self.__Blade_Knigth['Ene'] = 3
        return self.__Blade_Knigth
    
    def SmStatus(self,a,b = 2):
        if a == b:
            self.selectSM = a
            self.Forca += 3
            self.__Soul_Master['Str'] = 3
            self.Agilidade += 4
            self.__Soul_Master['Agi'] = 4
            self.Vitalidade += 3
            self.__Soul_Master['Vit'] = 3
            self.Energia += 10
            self.__Soul_Master['Ene'] = 10
            return self.__Soul_Master

    def MeStatus(self,a,b = 3):
        if a == b:
            self.selectMe = a
            self.Forca += 3
            self.__Muse_Elf['Str'] = 3
            self.Agilidade += 10
            self.__Muse_Elf['Agi'] = 10
            self.Vitalidade += 2
            self.__Muse_Elf['Vit'] = 2
            self.Energia += 5
            self.__Muse_Elf['Ene'] = 5
            return self.__Muse_Elf

    def MgStatus(self,a,b = 4):
        if a == b:
            self.selectMG = a
            self.Forca += 8
            self.__Magic_Gladiator['Str'] = 8
            self.Agilidade += 2
            self.__Magic_Gladiator['Agi'] = 2
            self.Vitalidade += 2
            self.__Magic_Gladiator['Vit'] = 2
            self.Energia += 8
            self.__Magic_Gladiator['Ene'] = 8
            return self.__Magic_Gladiator

        
             




    
        