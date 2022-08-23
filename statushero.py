
class status():
    def __init__(self):
        self.BK = {}
        self.SM = {}
        self.ME= {}
        self.MG = {}
        

    def statusBK(self):
        self.BK['str'] = 10
        self.BK['agi'] = 5
        self.BK['vit'] = 3
        self.BK['ene'] = 2
        return self.BK

    def statusSM(self):
        self.SM['str'] = 3
        self.SM['agi'] = 4
        self.SM['vit'] = 3
        self.SM['ene'] = 10
        return self.SM
    def statusMuse(self):
        self.ME = 3
        self.ME = 10
        self.ME = 2
        self.ME = 5
        return self.ME

    def statusMG(self):
        self.MG = 8
        self.MG = 2
        self.MG = 2
        self.MG = 8
        return self.MG