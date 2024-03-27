





from write import writing_file
from read import from_file_read_, reading_file,  userPhone_valid, Quantity_, id_,userName_valid
from datetime import datetime
laptop_dictionary = {}



# defining buy_function for option 1 when 1 is pressed
def buy_laptop():
    # when user enters option 1
    clients_Dictionary = []#definig the client dectionary to empty to store client information.
    Loop = True
    Laptop_Dictionary = reading_file()
    print("\t\t\t\t!!!WELCOME!!!")
    print("\n")
    print("\tPlease Provide Us Your Name And Contact Number To Prepare the invoice ")
    print("\n")
    Name = userName_valid()
    print("\n")
    Phone = userPhone_valid()
    print("\n")
    print("************************************************************************************************************************************************************")
    #for showing the items that are available in the store 
    print("S.N \t Name \t\t\t Brand \t\t\t Amount \t Quantity \t\t Processor \t\t Graphic Card")
    print("\n")
    from_file_read_()
    print("\n")
    print("***************************************************************************************************************************************************************")
    print("\n")

    while Loop == True:
        print("\n")
        id_valid = id_()
        print("\n")
        laptop_mass = int(input("Could You Let Us Know How Many Laptops Do You Required?:- "))
        print("\n")
        quantity__ = int(Laptop_Dictionary[id_valid][3])

        while laptop_mass <= 0 or laptop_mass > 20000:
            print("Valid quantity needed")
            
            print("\n")
            laptop_mass = int(input("Could You Let Us Know How Many Laptops Do You Required?:- "))
            quantity__ = int(Laptop_Dictionary[id_valid][3])
    

# Updating the Laptop_Dictionary Text Field.
        Laptop_Dictionary[id_valid][3] = int(Laptop_Dictionary[id_valid][3]) + int(laptop_mass)
       
        writing_file(Laptop_Dictionary)

        dateandtime = datetime.now()
        laptop_Name = Laptop_Dictionary[id_valid][0]
        quantity_ = laptop_mass
        unitexpenses_ = (Laptop_Dictionary[id_valid][2])#Unit Price
        expenses_ = Laptop_Dictionary[id_valid][2].replace("$", '')
        totalexpenses_ = int(expenses_) * int(quantity_)
        brandName = Laptop_Dictionary[id_valid][1]
        milliseconds = datetime.now().timestamp () * 100
        
        

        clients_Dictionary.append([laptop_Name, brandName, quantity_, unitexpenses_, expenses_, totalexpenses_])
        
        More = input("Do You Want More (Y/N):").upper()

        if More == "Y":
            Loop = True
        else:
            Loop = False

    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t***The Laptop Heaven PVT LTD.***")
    print("\n")
    print("\t\t\t 25Street SM Road UK \t |  Branch At Kamalpokhari, Kathmandu, Nepal")
    print("\n")
    print("#INVOICE : " + str(milliseconds))
    print("\n")
    print("Bill Date: " + str(dateandtime))
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Bill To: " + str(Name) + " \t\t\t\t\t\t\t\t\t\t Bill From: Sachida Paudel,Laptop Heaven")
    print("\n")
    print("Tel: " + str(Phone) + " \t\t\t\t\t\t\t\t\t\t\t\t Tel : +12 4567890")
    print("\n")
    print("********************************************************************************************************************************************************************")
    print("\n")
    print("\n")
    print("\n")
    print("S.N" + "\t\t" + "Product's Name" + "\t\t" + "Brand" + "\t  " + "Quantity" + "\t " + "Unit expenses_" + "\t\t\t" + "Amount")
    print("\n")
    a = 1
    total = 0
    for i in clients_Dictionary:
        print(str(a) + "\t\t" + str(i[0]) + "\t\t   " + str(i[1]) + "\t\t" + str(i[2]) + "\t\t\t" + str(i[3]) + "\t\t\t\t" + "$" + str(i[5]))
        a = a+1
        total = total +int(i[5])
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("** ATTENTION!! VAT is added to the Final Balance via 13% **")
    print("\n")
    print(" Final Balance: " + "\t\t" "$" + str(total)) # Net Amount
    vat_ = total * 0.13
    print("\n")
    print(" VAT Charge: " + "\t\t\t"   "$" + str(vat_)) #Vat amount
    #print("\n")
    print("_________________________________________________")
    print("\n")
    print(" Sum Total: " + "\t\t\t" "$" + str(total + vat_))
    print("_________________________________________________")
    print("\n")
    print("\n")
    print("--------**-----------------------------------**------")
    print("CRITERIA: Fund Once Paid Will Not Be Refunded. ")
    print("\n")
    print("PAYMENT METHOD")
    print("Account Number: XXXXX 00000 ####")
    print("National State Bank, UK")
    print("\n")
    print("----------**---------------------------------**-------")
    print("\n")
    print("\t\t\t\t\t @ if you have any queries about the invoice, Please contact")
    print("\t\t\t\t\t\t\t +12 3456 234, +13 56784 123 ")
    print("\t\t\t\t\t\t\t tlh23@icloud.com")
    print("\n")
    print("\n")
    print("\t\t\t\t\t We Are Glad To Have You!! Thank You For Supporting Our Business")
    print("\n")
    print("************************************************************************************************************************************************************************")
    print("\n")
    
    return id_valid, laptop_mass, Name, clients_Dictionary





# when user enters option 2


def sell_laptop():
    clients_Dictionary = [] #  empty for storing client information
    Loop = True
    Laptop_Dictionary = reading_file()
    print("Are You Excited To Shop? Yes We Are!!Lets Get Started")
    print("\n")
    print("We will need your name and contact number for the invoice.")
    print("\n")
    Name = userName_valid()
    print("\n")
    Phone = userPhone_valid()
    print("\n")

    print("S.N \t Name \t\t\t Brand \t\t\t expenses_ \t Quantity \t\t Processor \t\t Graphic Card")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    from_file_read_()

    print("\n")

    while Loop == True:
        
        print("\n")
        id_valid = id_()
        print("\n")
        laptop_mass = Quantity_()
        print("\n")
        _quantity_ = Laptop_Dictionary[id_valid][3]

        while laptop_mass <= 0 or laptop_mass > int(_quantity_):
            print("Dear Client, With regreat the quantitty you are looking for is not available.")
            print("\n")
            laptop_mass = int(input("To Complete The Order Please Let Us Know The Quantity Of Laptop You Will Like To Order:  "))
        print("\n")

        # Update the text file

        Laptop_Dictionary[id_valid][3] = int(Laptop_Dictionary[id_valid][3]) - int(laptop_mass)

        # getting user purchased items
        writing_file(Laptop_Dictionary)
        dateandtime = datetime.now()
        laptop_Name = Laptop_Dictionary[id_valid][0]
        quantity_ = laptop_mass
        unitexpenses_ = Laptop_Dictionary[id_valid][2]
        expenses_ = Laptop_Dictionary[id_valid][2].replace("$", '')
        totalexpenses_ = int(expenses_) * int(quantity_)
        brandName = Laptop_Dictionary[id_valid][1]
        milliseconds = datetime.now().timestamp () * 100
        #dateandtime = datetime.now()
        

        clients_Dictionary.append([laptop_Name, brandName, quantity_, unitexpenses_, expenses_, totalexpenses_])
        More = input("Want To Buy More?(Y/N):  ").upper()

        if More == "Y":
            Loop = True
        else:
            Loop = False
            print("\n")

    deliver = input("Want Your Laptop To Be Shipped?(Y/N):").lower()

    if deliver == "Y".lower():
        print("\n")
        House_No = input("Kindly Provide us with your house number or colony name for the delivery:  ")
        print("\n")
        print("We Provide Two Kind Of Facility Via Land And Air")
        print("\n")
        #House_No = input("Please provide us your full address for the delivery:")
        print("\n")
        print("NOTE: For Air, delivery time may delay based on the weather condition..")
        print("\n")
        
        waytoDeliver = input("How do you want your laptop to be delivered??(L/A:)").lower()

        if waytoDeliver == "L".lower():
            ShippingCharge = 5000
            print("\n")
            print("Any number of laptops will be deliver")
            
        elif waytoDeliver == "A".lower():
            
            ShippingCharge = 7000
            print("\n")
            print("Laptops deliver may take longer time,")
            print("\n")

        else:
            print("\n")
            ShippingCharge =  0
            print("\n")
            print("Shipping will not be granted...!!!")
            

    
    #billing portion for option 2:
    else:
        ShippingCharge =  0
        House_No = None
        print("\t\t\tDo Help Our Business Grow. Thank You!!!")

    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t-- The Laptop Heaven PVT LTD. -- ")
    print("\n")
    print("\t\t\t\t 25Street SM Road UK |  Branch At Kamalpokhari, Kathmandu, Nepal")
    print("\n")
    print("INVOICE: " + str(milliseconds) + "\t\t\t\t\t\t\t\t\t" + str(dateandtime))
    print("\n")
    print("Tel: +12 5678 1112, Laptop Heaven,UK")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Bill To: " + str(Name) )
    print("Address: "+ str(House_No))
    print("Tel: " + str(Phone))
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N" + "\t\t" + "Laptop's Name" + "\t\t" + "Brand Name" + "\t" + "Laptop Quantity" + "\t\t" + "Unit expenses_" + "\t\t" + "Total Expenses")
    print("\n")
    a = 1
    total = 0
    for i in clients_Dictionary:
        print(str(a) + "\t\t" + str(i[0]) + "\t\t" + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t\t" + "$" + str(i[5]))
        a = a+1
        total = total+int(i[5])
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("-------------------------------------------------------")
    print("\n")
    print("Final Balance: " + "\t\t\t" + "$" + str(total))#Net amount
    print("Shipping Charge:" + "\t\t" +"$" + str(ShippingCharge))#shipping amount
    print("______________________________________________________")
    print("Sum Total:" + "\t\t\t", "$" + str(total + ShippingCharge))#grand total
    print("______________________________________________________")
    print("\n")
    print("\n")
    print("--------**-----------------------------------**------")
    print("CRITERIA: Fund Once Paid Will Not Be Refunded. ")
    print("\n")
    print("PAYMENT METHOD")
    print("Account Number: XXXXX 00000 ####")
    print("National State Bank, UK")
    print("\n")
    print("----------**---------------------------------**-------")
    print("\n")
    print("\t\t\t\t\t @ if you have any queries about the invoice, Please contact")
    print("\t\t\t\t\t\t\t +12 3456 234, +13 56784 123 ")
    print("\t\t\t\t\t\t\t tlh23@icloud.com")
    print("\n")
    print("\n")
    print("\t\t\t\t\t We Are Glad To Have You!! Thank You For Supporting Our Business")
    print("\n")
    print("************************************************************************************************************************************************************************")
    print("\n")
    return id_valid, laptop_mass, Name, Phone, House_No, ShippingCharge, clients_Dictionary

    












