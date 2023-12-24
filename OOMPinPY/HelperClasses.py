import logging
#logging.basicConfig( level=logging.DEBUG)
#logging.basicConfig( level=logging.WARNING)
class BasicParkingLot:
    isOccupied:bool
    id:str
    type:str
    lon:float
    lat:float
    max_length:float
    max_wingspan:float
    def __init__(self, id, type, lon=0, lat=0, maxlen=0, maxwing=0, oc=False):
        self.id = id
        self.type = type
        self.lat = lat
        self.lon = lon
        self.max_length = maxlen
        self.max_wingspan = maxwing
        self.isOccupied = oc
        logging.debug("Basic Konstruktor")
        pass
class Aussenparkplatz(BasicParkingLot):
    power_available:bool
    shuttle_time:int
    def __init__(self, id, type, lon=0, lat=0, maxlen=0, maxwing=0, oc=False, pa=False, st=0):
        super().__init__(id, type, lon, lat, maxlen, maxwing, oc) 
        self.power_available = pa
        self.shuttle_time = st   
    def printObject(self):
        print("ID: ", self.id)
        print("Typ: ", self.type)
        print("Lon: ", self.lon)
        print("Lat: ", self.lat)
        print("Max Length: ", self.max_length)
        print("Max Wing: ", self.max_wingspan)
        print("Power Av: ", self.power_available)
        print("ShuttleTime:", self.shuttle_time)

class Terminalparkplatz(BasicParkingLot):
    fuel_available:bool
    numb_jetbridged:int
    def __init__(self, id, type, lon=0, lat=0, maxlen=0, maxwing=0, oc=False, fa=False, njb=1):
        super().__init__(id, type, lon, lat, maxlen, maxwing, oc)
        self.fuel_available = fa
        self.numb_jetbridged = njb
    def printObject(self):
        print("ID: ", self.id)
        print("Typ: ", self.type)
        print("Lon: ", self.lon)
        print("Lat: ", self.lat)
        print("Max Length: ", self.max_length)
        print("Max Wing: ", self.max_wingspan)
        print("Fuel Av: ", self.fuel_available)
        print("Numb Jetbridges:", self.numb_jetbridged)

import json
class Manager:
    listOfParkingLots:list
    filePath:str
    def __init__(self, filepath):
        """
        Intern ListOfAllParkingLots
        :param filepath for the document
        :note load json object, which is a dict with parking_positions and list of dict's with all values 
        """
        self.filePath = filepath
        self.listOfParkingLots = []
        with open(filepath, "r") as file:
            obj = json.load(file)
            data = obj.get('parking_positions')
        #print((data[0].get("id")))
        for item in data:
            """
            Iterate over all objects of the list with dictionarys to extract all Keyvalues and push them in the 
            fitting object of class
            """
            #print("inloop")
            id = item.get("id")
            typ = item.get("type")
            lon = item.get("lon")
            lat = item.get("lat")
            mLen = item.get("max_length")
            mWin = item.get("max_wingspan")
            oc = item.get("isOccupied")
            if (typ == "terminal"):
                fa = item.get("fuel_available")
                jb = item.get("number_of_jet_bridges")
                TermLot = Terminalparkplatz(id, typ, lon, lat, mLen, mWin, oc, fa, jb)
                self.listOfParkingLots.append(TermLot)
            if (typ =="outer"):
                pa = item.get("power_available")
                st = item.get("shuttle_time")
                AusLot = Aussenparkplatz(id, typ, lon, lat, mLen, mWin, oc, pa, st)
                self.listOfParkingLots.append(AusLot)
        print(len(self.listOfParkingLots), " Objekte erkannt")
    def printObjects(self):
        for object in self.listOfParkingLots:
            object.printObject()
            print("____________")
    def printOccupied(self):
        for object in self.listOfParkingLots:
            if object.isOccupied:
                print(object.id)
    def printFree(self):
        for object in self.listOfParkingLots:
            if not object.isOccupied:
                print(object.id)
    def CeckIn(self):
        self.printFree()
        lang = float(input("Wie lang ist das Flugzeug?"))
        spann = float(input("Welche Spannweite hat es?"))
        for object in self.listOfParkingLots:
            if not object.isOccupied and object.max_wingspan >= spann and object.max_length >= lang:
                print(object.id, " is free")
        checkin = input("Which would u like to check in?")
        for object in self.listOfParkingLots:
            if checkin in object.id:
                object.isOccupied = True
    def CheckOut(self):
        self.printOccupied()
        checkout = input("Which would u like to check out?")
        for object in self.listOfParkingLots:
            if checkout in object.id:
                object.isOccupied = False
    def Close(self):
        """
        Close Function
        :note Every Object is appended in a list as a dictionariy
        Then this List is the coresponding value to the key parking_positions, which is then write to output file via 
        json dump method
        """
        out_list = []
        for object in self.listOfParkingLots:
            out_list.append(object.__dict__)
        dic = {"parking_positions":out_list}
        with open("Outfile.json", "w") as file:
            json.dump(dic, file, indent=4)
    """
    Showing the user interface
    """
    def userInterface(self):
        print("Pleasse choose an action:\n1. CheckIn an aircraft\n2. CheckOut an aircraft\n3. List parkingpositions\n4. List free parkingpositions\n5. List occupied parkingpositions\n6. Colse Manager")
        userinput = int(input())
        match userinput:
            case 1:
                self.CeckIn()
            case 2:
                self.CheckOut()
            case 3:
                self.printObjects()
                pass
            case 4:
                self.printFree()
                pass
            case 5:
                self.printOccupied()
            case 6:
                self.Close()
                return False
        return True



 
"""
For Testing
"""
import HelperClasses as HC
#filePath = "/home/nils/PhythonWPF/OOMPinPY/example_airport.json"
filePath = "/home/nils/PhythonWPF/Outfile.json"
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    Man = HC.Manager(filePath)
    #Man.printObjects()
    try:
        while(Man.userInterface()):
            pass#
    except:
        logging.critical("FEHLER ALARM")