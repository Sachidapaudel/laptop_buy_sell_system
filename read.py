







def welcome_():
    
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t Welcome to The Laptop Heaven, Where Laptop Meets Affordibility")
    print("\n")
    print("\t\t\t\t\t\t 25street SM Road UK, London ")
    print("\n")
    print("\t\t\tThank You For Choosing Our Business. We Look Forward To Serving You :)")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")


def reading_file():
    Laptop_Dictionary = {}#Creating empty dictionary
    file = open("laptop.txt", "r")
    valid_id = 1
    for line in file:
        line = line.replace("\n", "")
        Laptop_Dictionary[valid_id] = line.split(",")
        valid_id += 1
    return Laptop_Dictionary





def from_file_read_():
    a = 1
    file = open("laptop.txt", "r")
    for line in file:
        print(a, "\t "+line.replace(",", "\t\t"))
        a += 1
    file.close()



 



#For valid phone number of the user:
def userPhone_valid():
    while True:
        print("\n")
        Phone = input("Input Your Phone Number Please:  ")
        try:
            int(Phone)
            return Phone
        except ValueError:
            print("\n")
            print("INVALID!! Please Check And Try Again :))")



#for Quantity of the Laptop

def Quantity_():
    while True:
        try:

            print("\n")
            laptop_mass = int(input("How Many Quantites Of Laptop Do You Want?:  "))
            print("\n")

            return laptop_mass
        except ValueError:
            print("\n")
            print("INVALID!! Please provide the valid quantity of the laptop you will like to order. ")
            print("\n")
    
    
            




    

# for id of user:

def id_():
    while True:
        try:

            print("\n")
            id_valid = int(input("Could You Please Provide the laptop Id Model You Wish To Buy: "))
            print("\n")

            if id_valid <= 0 or id_valid > len(reading_file()):
                print("\n")
                print("INVALID!!! Try Again:))")
        
                print("\n")
            else:
                return id_valid
            print("\n")
        except ValueError:
            print("\n")
        
            print("Sorry!! You have entered an un usual id. Try Again!!!")



# For Valid name  of the user: 
def userName_valid():
    while True:
        print("\n")
        Name = input("Please Input Your Name To Continue: ")
        try:
            int(Name)
        except ValueError:
            return Name
        print("\n")
        print("INVALID!!! Try Again:)")

 










        

