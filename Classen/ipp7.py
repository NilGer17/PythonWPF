#! usr/bin/python3

class Fahrzeug:
    #Typ-Anotation
    gewicht : int #in [kg]
    _leistung : float
    #__init__ muss immer sein! (Konstruktor)
    def __init__(self, Gewicht=0.0, Leistung=00):
        #print("__init__")
        self.gewicht = int(Gewicht)
        self._leistung = Leistung
        pass
    def print(self):
        print("Gewicht:", self.gewicht, "Leistung:", self._leistung)
    #Falls Klasenobjekt iwo aufgerufen wird und string fordert
    def __str__(self):
        return "Hallo"
    def calcLeistungsgewicht(self):
        if self._leistung > 0:
            return self.gewicht/self._leistung
        else:
            #print("Brudi mehr Leistung!")
            return 0.0
##################################
class Pkw(Fahrzeug):
    anz_achsen : int
    def __init__(self, Gewicht=0, Leistung=0, anzAchs =2):
        super().__init__(Gewicht, Leistung)
        self.anz_achsen = anzAchs
    def print(self):
        print("Gewicht:", self.gewicht, "Leistung:", self._leistung, "Achsen:", self.anz_achsen)
##################################
class Lkw(Fahrzeug):
    anz_achsen : int
    nutzlast:float
    def __init__(self, Gewicht=0, Leistung=0, anzAchs=6, nutz=3.5):
        super().__init__(Gewicht, Leistung)
        self.anz_achsen = anzAchs
        self.nutzlast = nutz
    def print(self):
        print("Gewicht:", self.gewicht, "Leistung:", self._leistung, "Achsen:", self.anz_achsen, "Nutzlast:", self.nutzlast)
####################################




Fzg1 = Fahrzeug(Gewicht=1200.9)
Fzg2 = Fahrzeug(1000.0, 777)
Fzg1.print()
Fzg2.print()

Fzg1.gewicht = 0.0
Fzg1._leistung = 10
Fzg1.print()

PKW1 = Pkw(9000, 230)
LKW1 = Lkw(Gewicht=4500, Leistung=400, anzAchs=12, nutz=40)

PKW1.print()
LKW1.print()
print("Leistungsgewicht:", Fzg1.calcLeistungsgewicht(), "kW/kg")
print("Leistungsgewicht:", Fzg2.calcLeistungsgewicht(), "kW/kg")
print("Leistungsgewicht:", PKW1.calcLeistungsgewicht(), "kW/kg")
print("Leistungsgewicht:", LKW1.calcLeistungsgewicht(), "kW/kg")
