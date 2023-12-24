import HelperClasses as HC
import logging
#filePath = "/home/nils/PhythonWPF/OOMPinPY/example_airport.json"
filePath = "OOMPinPY/Outfile.json"
if __name__ == "__main__":
    logging.basicConfig( level=logging.WARNING)
    Man = HC.Manager(filePath)
    #Man.printObjects()
    try:
        while(Man.userInterface()):
            pass
    except:
        logging.critical("FEHLER ALARM")