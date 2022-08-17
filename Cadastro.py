class Cadastro:
    def __init__(self):
        self.register = {}
        self.value = []

    
    def addKeyValue(self,a,b):
            self.value.append(b)    
            self.register[a] = self.value  
            return self.register

    def removeKeyValue(self,x):
        del self.register[x] 
        return self.register
