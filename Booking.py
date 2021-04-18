import pandas as pds
from datetime import timedelta,datetime
class Booking:

    def __init__(self, model, type1, file):
        self.file = file
        self.model=model
        self.type=type1

    def token(self,time):
        self.data=pds.read_excel(self.file)
        headers=self.data.columns.tolist()
        flag=0
        data=self.data.values.tolist()
        for item in data:
            if item[1].lower()==self.model.lower() and item[2].lower()==self.type.lower() and item[3].lower()=='available' :
                item[3]='Not Available'
                item[6]=time
                price=item[4]
                flag=1
                break
        if flag==1:
            data=pds.DataFrame(data,columns=headers)
            try:
                data.to_excel(self.file,index=False)
                return item[8],(price*4)
            except:
                print("Check if the file is opened in other window/tab")
        else:
            return str("Car Not Available")

class returning:
    def __init__(self,file):
        self.file=file
    def returnCar(self,token, MileReading, StartTime, ReturnTime):
        self.data = pds.read_excel(self.file)
        headers = self.data.columns.tolist()
        data = self.data.values.tolist()
        flag = 0
        for item in data:
            if item[8] == token and item[3].lower() == 'not available':
                item[3] = 'Available'
                oldReturnTime = item[6]
                item[6] = ''
                phr = item[4]
                pkm = item[5]
                oldMileReading = int(item[7])
                item[7] = MileReading
                flag = 1
                price = returning.priceCal(StartTime,ReturnTime,oldReturnTime,MileReading,oldMileReading,phr,pkm)
                adv = phr*4
                break
            elif item[3].lower() == 'available' and item[8] == token:
                print("You are returning an available car..\nEnter a valid token number")
                break
        if flag == 1:
            data = pds.DataFrame(data, columns=headers)
            try:
                data.to_excel(self.file, index=False)
                return price,adv
            except:
                print("Check if the file is opened in other window/tab")
        else:
            return str("Invalid Token Number")

    def priceCal(StartTime,ReturnTime,oldReturnTime,MileReading,oldMileReading,phr,pkm):
        price1=(MileReading-oldMileReading)*pkm
        StartTime = returning.validateTime(StartTime)
        ReturnTime = returning.validateTime(ReturnTime)
        x = ReturnTime-StartTime
        z = timedelta.total_seconds(x)
        price2 = int((z/3600)*phr)
        if price1 > price2:
            return price1
        elif price1 < price2:
            return price2
        else:
            return price2

    def validateTime(time):
        date = str(datetime.now()).split(' ')[0]
        while (True):
            try:
                if int(time.split(':')[0]) > 24 or int(time.split(':')[1]) > 60 or int(time.split(':')[0]) < 0:
                    print("Invalid time format")
                else:
                    break
            except:
                print("Time should be numerical only")
                return
        time = date + ' ' + time
        x = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        return x
