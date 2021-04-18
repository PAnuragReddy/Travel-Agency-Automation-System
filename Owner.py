import pandas as pds
from Car import Car

class Owner:
    
    def __init__(self, file):
        self.name = "Anurag"
        self.password = "PP"
        if(file == "DataCars.xlsx"):
            self.file = file
            self.rfile = "DataRecord.xlsx"
        elif(file == "DataRecord.xlsx"):
            self.rfile = file
            self.file = "DataCars.xlsx"
        self.data = pds.read_excel(self.file)
        self.rdata = pds.read_excel(self.rfile)
        
    def getData(self,car = None):
        if(car is None):
            ndata = self.data[["Sl No","Model","Type","Status"]]
            # print(ndata.to_string(index = False))
            return ndata
        elif(car.getModel() == "Invalid"):
            return None 
        else:
            model = car.getModel()
            Type = car.getType()
            if(((self.data['Model'] == model) & (self.data['Type'] == Type)).any()):
                ndata = self.data.loc[(self.data['Model'] == model) & (self.data['Type'] == Type)]
                ndata = ndata[["Sl No","Model","Type","Status"]]
                ndata.reset_index(inplace = True, drop = True)
                return ndata
            else:
                print("\nPlease enter correct Model and Type ")
                return None
            
                
        
    def updateData(self,car):
        if(car.getModel() == "Invalid"):
            return None
        else:
            print("Choose 1 to sell cars")
            print("Choose 2 to buy cars")
            choice = input("Do you want to sell or buy the car: ")
            
            if(choice == "2"):
                n = input("How many do you want to buy: ")
                n = int(n)
                snum = self.data.iloc[-1]["Sl No"]
                demand,mCharges,profit = car.getStats()
                pph,ppk = car.getPrice()
                for i in range(1,n+1):
                    Dict = {'Sl No' : snum + i, 'Model' : car.getModel(), 'Type' : car.getType(), 'Status' : 'Available',
                            'Average Demand per Week' : demand,'Average fuel efficiency(Km/L)' : car.getFeff(),
                            'Average Maintenance Expenses per Week(Rupees)' : mCharges, 'Price(Per Hour)' : pph,
                            'Price(Per Km)' : ppk,'Profit(Per Week)' : profit}
                    RDict = {'Sl No' : snum + i, 'Model' : car.getModel(), 'Type' : car.getType(), 'Status' : 'Available',
                             'Price(Per Hour)' : pph,'Price(Per Km)' : ppk,'Return time' : "", 'Mile Reading': 0, 'Token number' :snum + i}
                    self.data.loc[len(self.data.index)]=list(Dict.values())
                    self.rdata.loc[len(self.data.index)]=list(RDict.values())
                print("Successfully Bought")
                self.data.reset_index(inplace = True, drop = True)
                self.data.to_excel(self.file,index = False)
                self.rdata.reset_index(inplace = True, drop = True)
                self.rdata.to_excel(self.rfile,index = False)
                return self.data
                
                
            elif(choice == "1"):
                n = input("How many do you want to sell: ")
                n = int(n)
                count = 0
                index_names = self.data[ (self.data["Model"] == car.getModel()) & (self.data["Type"] == car.getType())].index
                for i in index_names:
                    count += 1
                    self.data.drop(i, inplace = True)
                    self.rdata.drop(i, inplace = True)
                    if(count == n):
                        break
                self.data.loc[index_names[0]:,'Sl No'] -= n
                self.rdata.loc[index_names[0]:,'Sl No'] -= n
                print("Successfully Sold")
                self.data.reset_index(inplace = True, drop = True)
                self.data.to_excel(self.file,index = False)
                self.rdata.reset_index(inplace = True, drop = True)
                self.rdata.to_excel(self.rfile,index = False)
                return self.data
            
            
            
    def getInfo(self,car):
        if(car.getModel() == "Invalid"):
            return None
        else:
            model = car.getModel()
            Type = car.getType()
            if(((self.data['Model'] == model) & (self.data['Type'] == Type)).any()):
                ndata = self.data.loc[(self.data['Model'] == model) & (self.data['Type'] == Type)]
                ndata = ndata[["Sl No","Model","Type","Status","Average Demand per Week","Average Maintenance Expenses per Week(Rupees)","Profit(Per Week)"]]
                return(ndata)
            else:
                return None
        
    def setPrice(self,car):
        if(car.getModel() == "Invalid"):
            return None
        else:
            print("Choose 1 to set Price per Hour")
            print("Choose 2 to set Price per Km")
            pph,ppk = car.getPrice()
            choice = input("Choice: ")
            if(choice == "1"):
                print("Present Price:",end=" ")
                print(pph)
                print(self.getInfo(car).to_string(index = False))
                nprice = input("Enter new price: ")
                nprice = int(nprice)
                self.data.loc[(self.data.Model == car.getModel()) & (self.data.Type == car.getType()), "Price(Per Hour)"] = nprice
                self.rdata.loc[(self.data.Model == car.getModel()) & (self.data.Type == car.getType()), "Price(Per Hour)"] = nprice
                
                
            elif(choice == "2"):
                print("Present Price:",end=" ")
                print(ppk)
                print(self.getInfo(car).to_string(index = False))
                nprice = input("Enter new price: ")
                nprice = int(nprice)
                self.data.loc[(self.data.Model == car.getModel()) & (self.data.Type == car.getType()), "Price(Per Km)"] = nprice
                self.rdata.loc[(self.data.Model == car.getModel()) & (self.data.Type == car.getType()), "Price(Per Km)"] = nprice
            
            
            print("Price Changed Successfully")
            self.data.to_excel(self.file,index = False)
            self.rdata.to_excel(self.rfile,index = False)
            return self.data
            

# car = Car("Tata Sumo","AC","DataCars.xlsx")
# me = Owner("DataCars.xlsx")
# df = me.setPrice(car)
