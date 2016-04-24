import coordinate

class Bounds():

    def __init__(self, UL, UR, DL, DR):
        self.UL = UL
        self.UR = UR
        self.DL = DL
        self.DR = DR

    def GetUL(self):
        return self.UL

    def GetUR(self):
        return self.UR

    def GetDL(self):
        return self.DL

    def GetDR(self):
        return self.DR
