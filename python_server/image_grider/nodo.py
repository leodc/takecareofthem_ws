import coordinate as coor


class Nodo():

    def __init__(self, lat, lng):
        self.center = coor.Coordinate(lat, lng)
        self.neig_00;
        self.neig_01;
        self.neig_02;
        self.neig_10;
        self.neig_12;
        self.neig_20;
        self.neig_21;
        self.neig_22;

    def GetCoors(self):
        return self.center

    def GetWeight(self):
        return self.weights

    def SetNe00(self, neig_00):
        self.neig_00 = neig_00

    def SetNe01(self, neig_01):
        self.neig_01 = neig_01

    def SetNe02(self, neig_02):
        self.neig_02 = neig_02

    def SetNe10(self, neig_10):
        self.neig_10 = neig_10

    def SetNe12(self, neig_12):
        self.neig_12 = neig_12

    def SetNe20(self, neig_20):
        self.neig_20 = neig_20

    def SetNe21(self, neig_21):
        self.neig_21 = neig_21

    def SetNe22(self, neig_22):
        self.neig_22 = neig_22


