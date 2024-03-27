






from read import reading_file,userPhone_valid, Quantity_,id_,userName_valid
from datetime import datetime


def writing_file(Laptop_Dictionary):
    
    file = open("laptop.txt", "w")
    for values in Laptop_Dictionary.values():
        file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]))
        file.write("\n")
    file.close()



# for bill printing when option1 is presses. 
def bill_buy(id_valid, laptop_mass, Name, clients_Dictionary):

    Laptop_Dictionary = reading_file()

    dateandtime = datetime.now()
    milliseconds = datetime.now().timestamp () * 100
    laptop_Name = Laptop_Dictionary[id_valid][0]
    quantity_ = laptop_mass
    unitexpenses_ = (Laptop_Dictionary[id_valid][2])
    expenses_ = Laptop_Dictionary[id_valid][2].replace("$", '')
    totalexpenses_ = int(expenses_) * int(quantity_)
    #dateandtime = datetime.now()
    brandName = Laptop_Dictionary[id_valid][1]

    #clients_Dictionary.append([laptop_Name, brandName, quantity_, unitexpenses_, expenses_, totalexpenses_])

    with open(str(Name) + str(dateandtime) + ".txt", 'w') as file:
        file.write("\n")
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("***The Laptop Heven PVT LTD.***")
        file.write("\n")
        file.write("\t\t\t 25Street SM Road UK \t |  Branch At Kamalpokhari, Kathmandu, Nepal")
        file.write("\n")
        file.write("#INVOICE :" + str(milliseconds))
        file.write("\n")
        file.write("Bill Date: " + str(dateandtime))
        file.write("\n")
        file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")

        file.write("Bill To: " + str(Name) + " \t\t\t\t\t\t\t\t\t\t Bill From: Sachida Paudel,Laptop Heaven")
        file.write("\n")
        file.write("Tel: +34 67800 111" + " \t\t\t\t\t\t\t\t\t\t\t\t Tel : +12 4567890")
        file.write("\n")
        file.write("********************************************************************************************************************************************************************")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("S.N" + "\t\t" + "Laptop Name" + "\t\t" + "Brand Name" + "\t  " + "Laptop Quantity" + "\t " + "Unit expenses_" + "\t\t\t" + "Total Amount")
        file.write("\n")
        a = 1
        total = 0
        for i in clients_Dictionary:
            file.write(str(a) + "\t\t" + str(i[0]) + "\t\t   " + str(i[1]) + "\t\t" + str(i[2]) + "\t\t\t" + str(i[3]) + "\t\t\t\t" + "$" + str(i[5]))
            a = a+1
            total = total +int(i[5])
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("**NOTICE: VAT is added to the Final Balance via 13%**")
        file.write("\n")
        file.write(" Final Balance: " + "\t\t" "$" + str(total)) # Net Amount
        vat_ = total * 0.13
        file.write("\n")
        file.write(" VAT Charge: " + "\t\t\t"   "$" + str(vat_)) #Vat amount
    #file.write("\n")
        file.write("_________________________________________________")
        file.write("\n")
        file.write(" Sum Total: " + "\t\t\t" "$" + str(total + vat_))
        file.write("_________________________________________________")
        file.write("\n")
        file.write("\n")
        file.write("--------**-----------------------------------**------")
        file.write("CRITERIA: Fund Once Paid Will Not Be Refunded. ")
        file.write("\n")
        file.write("PAYMENT METHOD")
        file.write("Account Number: XXXXX 00000 ####")
        file.write("National State Bank, UK")
        file.write("\n")
        file.write("----------**---------------------------------**-------")
        file.write("\n")
        file.write("\t\t\t\t\t @ If you have any queries about the invoice, Please contact")
        file.write("\t\t\t\t\t\t\t +12 3456 234, +13 56784 123 ")
        file.write("\t\t\t\t\t\t\t tlh23@icloud.com")
        file.write("\n")
        file.write("\n")
        file.write("\t\t\t\t\t We Are Glad To Have You!! Thank You For Supporting Our Business")
        file.write("\n")
        file.write("************************************************************************************************************************************************************************")
        file.write("\n")



# For bill printing when option 2 is pressed.

def bill_sell(id_valid, laptop_mass, Name, Phone, House_No , ShippingCharge, clients_Dictionary):
    #dateandtime = datetime.now()
    #milliseconds = datetime.now().timestamp () * 100

    Laptop_Dictionary = reading_file()

    dateandtime = datetime.now()
    milliseconds = datetime.now().timestamp () * 100
    laptop_Name = Laptop_Dictionary[id_valid][0]
    quantity_ = laptop_mass
    unitexpenses_ = Laptop_Dictionary[id_valid][2]
    expenses_ = Laptop_Dictionary[id_valid][2].replace("$", '')
    totalexpenses_ = int(expenses_) * int(quantity_)
    brandName = Laptop_Dictionary[id_valid][1]
    

    #clients_Dictionary.append([laptop_Name, brandName, quantity_, unitexpenses_, expenses_, totalexpenses_])

    with open(str(Name) + str(dateandtime) + ".txt", 'w') as file:
        file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("\t\t\t\t\t-- The Laptop Heaven PVT LTD. -- ")
        file.write("\n")
        file.write("\t\t\t\t 25Street SM Road UK |  Branch At Kamalpokhari, Kathmandu, Nepal")
        file.write("\n")
        file.write("INVOICE: " + str(milliseconds))
        file.write("\n")
        file.write("Tel: +12 5678 1112, Laptop Heaven,UK")
        file.write("\n")
        file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("Bill To: " + str(Name) )
        file.write("Address: "+ str(House_No))
        file.write("Tel: " + str(Phone))
        file.write("\n")
        file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("S.N" + "\t\t" + "Laptop's Name" + "\t\t" + "Brand Name" + "\t\t   " + "Laptop Quantity" + "\t\t" + "Unit expenses_" + "\t\t" + "Total Expenses")
        file.write("\n")
        a = 1
        total = 0
        for i in clients_Dictionary:
            file.write(str(a) + "\t\t" + str(i[0]) + "\t\t" + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + "$" + str(i[5]) + "\n")
            a = a+1
            total = total+int(i[5])
        file.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("-------------------------------------------------------")
        file.write("\n")
        file.write("Final Balance: " + "\t\t\t" + "$" + str(total))#Net amount
        file.write("\n")
        file.write("Shipping Charge:" + "\t\t" +"$" + str(ShippingCharge))
        file.write("______________________________________________________")
        file.write("Sum Total:" + "\t\t\t" + "$" + str(total + ShippingCharge)) #grand total
        file.write("______________________________________________________")
        file.write("\n")
        file.write("\n")
        file.write("--------**-----------------------------------**------")
        file.write("CRITERIA: Fund Once Paid Will Not Be Refunded. ")
        file.write("\n")
        file.write("PAYMENT METHOD")
        file.write("Account Number: XXXXX 00000 ####")
        file.write("National State Bank, UK")
        file.write("\n")
        file.write("----------**---------------------------------**-------")
        file.write("\n")
        file.write("\t\t\t\t\t @ If you have any queries about the invoice, Please contact")
        file.write("\t\t\t\t\t\t\t +12 3456 234, +13 56784 123 ")
        file.write("\t\t\t\t\t\t\t tlh23@icloud.com")
        file.write("\n")
        file.write("\n")
        file.write("\t\t\t\t\t We Are Glad To Have You!! Thank You For Supporting Our Business")
        file.write("\n")
        file.write("************************************************************************************************************************************************************************")
        file.write("\n")
        
