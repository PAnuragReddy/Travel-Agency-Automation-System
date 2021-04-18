from Owner import Owner
from Car import Car
from Booking import Booking,returning
from Customer import Customer
import pandas as pds
from time import sleep
from datetime import datetime

file="DataRecord.xlsx"

def main():
    while(True):
        print("Are you owner or customer")
        print("1: Owner")
        print("2: Customer")
        print("3: Exit",end="")
        choice = input("\nEnter your choice : ")
        if(choice == '1'):
            owner = Owner("DataCars.xlsx")
            password = input("Enter Password:")
            if(password == owner.password):
                print("\nWelcome!!!")
                while(True):
                    print("\nWhat do you want to do?")
                    print("1: Look at database ")
                    print("2: Update database")
                    print("3: Get Info of Car")
                    print("4: Set price of a car")
                    print("5: Exit")
                    choice = input("Enter your choice: ")
                    
                    if(choice == '5'):
                        break
                    
                    elif(choice == '1'):
                        model = input("Enter Car Model: ")
                        Type = input("Enter Car Type: ")
                        car = Car(model,Type,"DataCars.xlsx")
                        if(model == ''):
                            print(owner.getData().to_string(index = False))
                        else:
                            if(owner.getData(car) is None):
                                print("\nPlease enter correct Model and Type ")
                            else:
                                print(owner.getData(car).to_string(index = False))
                    
                    elif(choice == '2'):
                        model = input("Enter Car Model: ")
                        Type = input("Enter Car Type: ")
                        car = Car(model,Type,"DataCars.xlsx")
                        #owner.updateData(car) == None
                        df = owner.updateData(car)
                        if(df is None):
                            print("\nPlease enter correct Model and Type ")
                        else:
                            continue
                            
                            
                    elif(choice == '3'):
                        model = input("Enter Car Model: ")
                        Type = input("Enter Car Type: ")
                        car = Car(model,Type,"DataCars.xlsx")
                        if(owner.getInfo(car) is None):
                            print("\nPlease enter correct Model and Type ")
                        else:
                            print(owner.getInfo(car).to_string(index = False))
                        
                    elif(choice == '4'):
                        model = input("Enter Car Model: ")
                        Type = input("Enter Car Type: ")
                        car = Car(model,Type,"DataCars.xlsx")
                        df = owner.setPrice(car)
                        if(df is None):
                            print("\nPlease enter correct Model and Type ")
                        else:
                            continue
                            
            else:
                print("Please enter the correct password")
                
            # print("\nWhat do you want to do?")
            # print("1:")
        elif(choice == '2'):
            print("Welcome to TAAS")
            cars_data=pds.read_excel(file)
            while (True):
                print("\nWhat do you want to do?")
                print("1: Book a Car ")
                print("2: Return a Car")
                print("3: Exit")
                choice = input("Enter your choice: ")
                if (choice == '3'):
                    break
                elif (choice == '1'):
                    print("1. Ask for certain car")
                    print("2. Show all available Cars")
                    print("3. Exit")
                    choice1 = input("Enter your choice: ")
                    if (choice1 == '1' or choice1 == '2'):
                        if choice1=='2':
                            print("Available Cars: \n")
                            available_cars = pds.DataFrame(cars_data[cars_data['Status'] == 'Available'],
                                                           columns=['Model', 'Type', 'Price(per hour)', 'Price(per Km)'])
                            print(available_cars.drop_duplicates(subset=['Model', 'Type'], keep='first'))
    
                        model = input("Enter Car Model: ")
                        type = input("Enter Car Type: ")
                        print("Do you want to book " + model + " " + type + " car ?\n1. Yes\n2. No")
                        choice11=input("Enter your choice: ")
                        if (choice11 == "1"):
                            cars=cars_data.values.tolist()
                            for item in cars:
                                if item[1].lower() == model.lower() and item[2].lower() == type.lower() and item[3].lower() == 'available':
                                    available="1"
                                    break
                                else:
                                    available ="0"
                            if available == "1":
                                print("Car is Available")
                                rtime = str(input("enter Expected return time in HH:MM:SS format :"))
                                b = Booking(model, type, file)
                                booking_id,price = b.token(rtime)
                                print("Pay Advance Amount: " + str(price))
                                sleep(3)
                                print("Your Token Number is " + str(booking_id))
                                print("Collect your Car\nThanks for visiting :)")
                            elif available == "0":
                                print("Car Not Available/Invalid Car, Try Again..")
                        else:
                            print()
    
                    elif (choice1 == '3'):
                        break
                    else:
                        print('Invalid Choice. Try again')
    
                elif (choice == '2'):
                    token = int(input("Enter Token number: "))
                    MileReading = int(input("Enter Mile reading: "))
                    StartTime = str(input("enter Car pick up time in HH:MM:SS format :"))
                    ReturnTime = str(input("enter return time in HH:MM:SS format :"))
                    ret=returning(file)
                    price,adv = ret.returnCar(token, MileReading, StartTime, ReturnTime)
                    final=abs(price-adv)
                    sleep(2)
                    print("------ Bill ------")
                    print("  price           : "+str(price))
                    print("  Advance amount  : "+str(adv))
                    print("---------------------------")
                    if(price > adv ):
                        print("  you need to pay : "+str(final))
                    elif(price < adv):
                        print("  you need to get: " + str(final))
                    elif(price == adv):
                        print("  you need to pay nothing ")
                    print("---------------------------")
                    print()
                    sleep(3)
                    print("Thanks for Visiting :)")
                else:
                    print("Invalid Choice.. Try again.")
        
        elif(choice == '3'):
            break





if __name__ == '__main__':
    main()