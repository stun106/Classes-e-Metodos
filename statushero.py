from classeperson import ClasseHero
class status(ClasseHero):
    def __init__(self):
        ClasseHero.__init__(self)
        self.Forca = 0
        self.Agilidade = 0
        self.Vitalidade = 0
        self. Energia = 0

        
    def BkStatus(self): #<- Função que atribui status no heroi BladeKnigth na classe herdada , e predertemina cada status individualmente na classe"status"
        self.Forca += 10
        self.Blade_Knigth['Str'] = 10 
        self.Agilidade += 5
        self.Blade_Knigth['Agi'] = 5
        self.Vitalidade += 3
        self.Blade_Knigth['Vit'] = 3
        self.Energia += 2
        self.Blade_Knigth['Ene'] = 2
        return self.__Blade_Knigth

    def SmStatus(self):
        self.Forca += 2
        self.__Soul_Master['Str'] = 3
        self.__Soul_Master += 5
        self.__Soul_Master['Agi'] = 4
        self.Vitalidade += 3
        self.__Soul_Master['Vit'] = 3
        self.Energia += 2
        self.__Soul_Master['Ene'] = 10
        return self.__Soul_Master

    def MeStatus(self):
        self.Forca += 3
        self.__Muse_Elf['Str'] = 3
        self.Agilidade += 10
        self.__Soul_Master['Agi'] = 10
        self.Vitalidade += 2
        self.__Soul_Master['Vit'] = 2
        self.Energia += 5
        self.__Soul_Master['Ene'] = 5
        return self.__Soul_Master
    
    def MgStatus(self):
        self.Forca += 8
        self.__Magic_Gladiator['Str'] = 8
        self.Agilidade += 2
        self.__Magic_Gladiator['Agi'] = 2
        self.Vitalidade += 2
        self.__Magic_Gladiator['Vit'] = 2
        self.Energia += 8
        self.__Magic_Gladiator['Ene'] = 8
        return self.__Soul_Master

