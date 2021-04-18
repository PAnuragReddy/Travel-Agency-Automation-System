import pandas as pds
from Booking import Booking
from Car import Car

class Customer:
    def __init__(self,file,token):
        self.name="Abhiram"
        self.file= file
        self.token=token

    def getAvailableCars(self):
        status = "Available"
        if (self.data["Status"] == status).any():
            ndata = self.data.loc[(self.data['Status'] == status)]
            ndata = ndata[["Model", "Type", "Status", "Price(per hour)", "Price(per Km)"]]
            df = pds.DataFrame(data=ndata)
            print(df.drop_duplicates(subset=['Model', 'Type'], keep='first'))

    def checkAvailability(self,model,type):
        if (((self.data['Model'] == model) & (self.data['Type'] == type)).any()):
            ndata = self.data.loc[(self.data['Model'] == model) & (self.data['Type'] == type) & (self.data['Status'] == 'Available')]
            ndata = ndata[["Model", "Type", "Status"]]
            if (ndata['Status'] == 'Available').any():
                return("Car is Available")
            else:
                return("Car is not Available")
        #print()




