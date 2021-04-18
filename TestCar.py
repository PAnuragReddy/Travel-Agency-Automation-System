import unittest
from Car import Car

class TestCar(unittest.TestCase):

	
    def test_getModel(self):
        car = Car("Honda City","Non-AC","TestDataCars.xlsx")
        model = car.getModel()
        self.assertEqual(model,'Honda City',f'Model is Honda City and not {model}')

    def test_getType(self):
        car = Car("Honda City","Non-AC","TestDataCars.xlsx")
        Type = car.getType()
        self.assertEqual(Type,'Non-AC',f'Type is Non-AC and not {Type}')
      
    def test_getPricePerHr(self):#per hour option 
        car = Car("Honda City","Non-AC","TestDataCars.xlsx")
        pph,ppk=car.getPrice()
        
        self.assertEqual(pph,300,f'price must be 300 and not {pph}')
    
    def test_getpricePerKm(self):#per mile option
          car = Car("Honda City","Non-AC","TestDataCars.xlsx")
          pph,ppk=car.getPrice()
          
          self.assertEqual(ppk,200,f'price must be 200 and not {ppk}')

    def test_getMR(self):
        car = Car("Honda City","Non-AC","TestDataCars.xlsx")
        MR=car.getMR()
        
        self.assertEqual(MR, None,f'MR must be 142 and not {MR}')

    def test_getStats(self):
        car = Car("Honda City","Non-AC","TestDataCars.xlsx")
        demand,mcharges,profits=car.getStats()
        self.assertEqual(demand,2,f'Demand must be 2 and not {demand}')
        self.assertEqual(mcharges,2000,f'Maintenance Expenses must be 2000 and not {mcharges}')
        self.assertEqual(profits,1000,f'Profits must be 1000 and not {profits}')


suite = unittest.TestLoader().loadTestsFromTestCase(TestCar)
unittest.TextTestRunner(verbosity=2).run(suite)
