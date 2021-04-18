import pandas as pds

class Car:
    
    def __init__(self,model_,Type_,file):
        
        self.file = file
        data = pds.read_excel(file)
        if((model_ in (data.Model.unique().tolist())) & (Type_ in (data.Type.unique().tolist()))):
            self.model = model_
            self.Type = Type_
            if(((data['Model'] == model_) & (data['Type'] == Type_)).any()):
                ndata = data.loc[(data['Model'] == model_) & (data['Type'] == Type_)]
                ndata.reset_index(inplace = True, drop = True)
                self.demand = ndata.loc[0,"Average Demand per Week"]
                self.mCharges = ndata.loc[0,"Average Maintenance Expenses per Week(Rupees)"]
                self.profit = ndata.loc[0,"Profit(Per Week)"]
                self.pph = ndata.loc[0,"Price(Per Hour)"]
                self.ppk = ndata.loc[0,"Price(Per Km)"]
                self.feff = ndata.loc[0,"Average fuel efficiency(Km/L)"]
            else:
                self.model = "Invalid"
        else:
            self.model = "Invalid"
        
    def getModel(self):
        return self.model
        
    def getFeff(self):
        return self.feff
    
    def getType(self):
        return self.Type
        
    def getPrice(self):
        return self.pph,self.ppk;        
        
    def getMR(self):
        None
        
    def getStats(self):
        return self.demand,self.mCharges,self.profit;

#car = Car("Tata Sumo","AC","DataCars.xlsx")
#print(car.getModel())
# file = "DataCars.xlsx"
# data = pds.read_excel(file)       
# print("Tata Sumo" in (data.Model.unique().tolist()))
