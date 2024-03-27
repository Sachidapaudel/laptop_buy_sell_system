


from read import welcome_,id_, Quantity_
from operation import buy_laptop, sell_laptop
from write import writing_file, bill_buy,bill_sell




#For welcome message 
welcome_()
print("\n")


#function that defines choises of users
def choose():

    Continue_Loop_ = True
    while Continue_Loop_ == True:
        print("\t   a) Click 1 To Purchase From The Suppliers")
        print("\t   b) Click 2 To Sell To Clients")
        print("\t   c) Press 3 To Exit")
        print("\n")

        choose = True
        while choose == True:
            try:
                chooseInput = int(input("\t Dear valued customer, please select from the available Options List:  "))
                print("\n")

                choose = False
            except:
                print("Alphabetical Values are not allowed!")

        if chooseInput == 1:
            id_valid, laptop_mass, Name, clients_Dictionary = buy_laptop()
            bill_buy(id_valid, laptop_mass, Name, clients_Dictionary)#pass return value of buy_laptop to buy_bill.

        elif chooseInput == 2:
            id_valid, laptop_mass, Name, Phone, House_No, ShippingCharge, clients_Dictionary = sell_laptop()
            bill_sell(id_valid, laptop_mass,Name, Phone, House_No, ShippingCharge, clients_Dictionary)#pass return value of buy_laptop to buy_bill.

        elif chooseInput == 3:
            Continue_Loop_ = False
            print("\n")
            print("Thank You For Being A Valued User Of Our Application!!Have a nice Day!!!")
            print("\n")

        else:
            print("Invalid Input!!Please Try Again")


choose()






            




