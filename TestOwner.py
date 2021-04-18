import pandas as pds
import unittest
from Car import Car
from Owner import Owner
from pandas.util.testing import assert_frame_equal

class TestOwner(unittest.TestCase):

    def test_getData_WI(self):#wrong input
        owner = Owner("TestDataCars.xlsx")
        wcar = Car("Mercedes","Non-AC","TestDataCars.xlsx")
        df = owner.getData(wcar)
        data = [[1,'Honda City','Non-AC','Available',2,18,2000,300,200,1000]]
        dfTest = pds.DataFrame(data, columns =['Sl No','Model','Type','Status','Average Demand per Week','Average fuel efficiency(Km/L)','Average Maintenance Expenses per Week(Rupees)','Price(Per Hour)','Price(Per Km)','Profit(Per Week)'])
        
        self.assertEqual(df,None,f'Data must be {dfTest} and not {df}')

    def test_getData_CI(self):#correct input
        owner = Owner("TestDataCars.xlsx")
        ccar = Car("Honda City","Non-AC","TestDataCars.xlsx")
        df = owner.getData(ccar)
        data = [[1,'Honda City','Non-AC','Available']]
        dfTest = pds.DataFrame(data, columns =['Sl No','Model','Type','Status'])
        assert_frame_equal(df,dfTest)
        

    def test_getData_NI(self):#No input
        owner = Owner("TestDataCars.xlsx")
        df = owner.getData()
        data = [[1,'Honda City','Non-AC','Available']]
        dfTest = pds.DataFrame(data, columns =['Sl No','Model','Type','Status'])
        assert_frame_equal(df,dfTest)
        

    def test_updateData_BCI(self):
        owner = Owner("TestDataCars.xlsx")
        ccar = Car("Honda City","Non-AC","TestDataCars.xlsx")
        print("Function to test Buying of Car by buying one new car")
        df = owner.updateData(ccar)
        data = [[1,'Honda City','Non-AC','Available',2,18,2000,350,250,1000],[2,'Honda City','Non-AC','Available',2,18,2000,350,250,1000]]
        dfTest = pds.DataFrame(data, columns =['Sl No','Model','Type','Status','Average Demand per Week','Average fuel efficiency(Km/L)','Average Maintenance Expenses per Week(Rupees)','Price(Per Hour)','Price(Per Km)','Profit(Per Week)'])
        
        assert_frame_equal(df,dfTest)

    def test_updateData_SCI(self):
        owner = Owner("TestDataCars.xlsx")
        ccar = Car("Honda City","Non-AC","TestDataCars.xlsx")
        print("Function to test Selling of Car by selling one car")
        df = owner.updateData(ccar)
        data = [[1,'Honda City','Non-AC','Available',2,18,2000,350,250,1000]]
        dfTest = pds.DataFrame(data, columns =['Sl No','Model','Type','Status','Average Demand per Week','Average fuel efficiency(Km/L)','Average Maintenance Expenses per Week(Rupees)','Price(Per Hour)','Price(Per Km)','Profit(Per Week)'])
        
        assert_frame_equal(df,dfTest)

    def test_getInfo_WI(self):
        owner = Owner("TestDataCars.xlsx")
        wcar = Car("Mercedes","Non-AC","TestDataCars.xlsx")
        df = owner.getInfo(wcar)
        info = [[1,'Honda City','Non-AC','Available',2,2000,1000]]
        dfInfoTest = pds.DataFrame(info, columns =['Sl No','Model','Type','Status','Average Demand per Week','Average Maintenance Expenses per Week(Rupees)','Profit(Per Week)'])
        
        self.assertEqual(df,None,f'Data must be {dfInfoTest} and not {df}')


    def test_getInfo_CI(self):
        owner = Owner("TestDataCars.xlsx")
        ccar = Car("Honda City","Non-AC","TestDataCars.xlsx")
        df = owner.getInfo(ccar)
        info = [[1,'Honda City','Non-AC','Available',2,2000,1000]]
        dfInfoTest = pds.DataFrame(info, columns =['Sl No','Model','Type','Status','Average Demand per Week','Average Maintenance Expenses per Week(Rupees)','Profit(Per Week)'])
        
        assert_frame_equal(df,dfInfoTest)

    def test_setPricePerKm_CI(self):
        owner = Owner("TestDataCars.xlsx")
        ccar = Car("Honda City","Non-AC","TestDataCars.xlsx")
        print("Function to test setting price per km, set to 250")
        owner.setPrice(ccar)#setting price to 250
        data = [[1,'Honda City','Non-AC','Available',2,18,2000,350,250,1000]]
        df = pds.DataFrame(data, columns =['Sl No','Model','Type','Status','Average Demand per Week','Average fuel efficiency(Km/L)','Average Maintenance Expenses per Week(Rupees)','Price(Per Hour)','Price(Per Km)','Profit(Per Week)'])
        
        self.assertEqual(df.loc[0,'Price(Per Km)'],250,f'Price must be 275 and not {int(df["Price(Per Km)"])}')
        
    def test_setPricePerHr_CI(self):
        owner = Owner("TestDataCars.xlsx")
        ccar = Car("Honda City","Non-AC","TestDataCars.xlsx")
        print("Function to test setting price per Hr, set to 350")
        owner.setPrice(ccar)#setting price to  350
        data = [[1,'Honda City','Non-AC','Available',2,18,2000,350,250,1000]]
        df = pds.DataFrame(data, columns =['Sl No','Model','Type','Status','Average Demand per Week','Average fuel efficiency(Km/L)','Average Maintenance Expenses per Week(Rupees)','Price(Per Hour)','Price(Per Km)','Profit(Per Week)'])
        
        self.assertEqual(df.loc[0,'Price(Per Hour)'],350,f'Price must be 350 and not {int(df["Price(Per Hour)"])}')
        

suite = unittest.TestLoader().loadTestsFromTestCase(TestOwner)
unittest.TextTestRunner(verbosity=2).run(suite)

