# -------------------
# Imp! There're Mainly Two Types of Relationships in classes of Python.

# Q. What're those relationship Types ? 
# Ans: Aggregation(Has - a) & Inheritance (Is - a). 

# e.g.) So, Say - we have a class called "Product" & "SmartPhones"
# *     That means, Smartphone "Is - a (Inheritance)" Product. 
# *     That means, SmartPhone Will be Inheriting the "Product" Class.

# e.g.) Other Famous Example of Inheritance is "Vehicle" Class
# *     That's inherited by "Car" Class.

# Q. Give An Example of Aggregation Type Relation in Python Class.
# e.g.) Let's Say there's a Class "Customer" & "Address"
# *     That means Customer "Has - a (Aggregation)" Address.
# *     That means the relation type is Aggregation. 


# Imp! Craft Class "Customer" & "Address" With Aggregation Relation. 

class Customer: 
    def __init__(self, name, gender, Address):

        self.name = ""
        self.gender = ""

        self.set_name(name)
        self.set_gender(gender)
        self.set_address(Address)

    def set_name(self, name):
        set = False
        if (type(name) is str):
            self.name = name 
            set = True
        else:
            print("Invalid Name Value.")
            return set

    def set_gender(self, gender): 
        set = False 
        if (type(gender) == str):
            if (len(gender) == 1):
                if (gender.upper() == "M" or gender.upper() == "F"):
                    self.gender = gender
                    set = True

        if (set == False):
            print("bad Value for Gender Field (Enter only M/F).")
        
        return set

    def set_address(self, addr):
        set = False
        if (isinstance(addr, Address) is True):
            self.addr = addr
            set = True
        else: 
            print("Please Do Pass The Instance of Address.")

    def change_profile(self, new_name, new_gender, new_address): 
        self.set_name(new_name)
        self.set_gender(new_gender)
        self.set_address(new_address)


    def greet(self):
        if (self.addr != None):
            print(f"Hello, {self.name}", "Sir" if self.gender == "M" else "Ma'am")

            print(f"Address is {self.addr.city}, {self.addr.state}")

class Address:
    
    def __init__(self, city, state, pincode):

        self.city = ""
        self.state = ""
        self.pincode = 0
        
        self.set_city(city)
        self.set_state(state)
        self.set_pincode(pincode)

    def set_city(self, city):
        set = False
        if (type(city) is str):
            self.city = city 
            set = True
        else:
            print("Invalid City Value.")
        
        return set
    
    def set_state(self, state):
        set = False
        if (type(state) is str):
            self.state = state 
            set = True
        else:
            print("Invalid State Value")
            
        return set

    def set_pincode(self, pincode):
        set = False
        if (type(pincode) is int):
            if (pincode > 99999):
                self.pincode = pincode
                set = True
        
        if (set == False):
            print("Invalid Pincode.")
            return False

    def change_address(self, new_city, new_state, new_pin):
        set = False
        set = self.set_city(new_city)
        if (set != False):
            set = self.set_state(new_state)
            
            if (set != False):
                set = self.set_pincode(new_pin)
        
        return set
        


if __name__ == "__main__":
    addr1 = Address("Ahmedabad", "Gujarat", 201206)
    addr2 = Address("City of Fear", "Fear State", 666666)

    customer1 = Customer("Prithvee", "M", addr1)
    customer2 = Customer("xyz", "F", addr2 )

    customer1.greet()
    if (customer1.addr.change_address(1212, "Gujarat", 370201) == False):
        print("Unable To Change Address.")
    
    if (customer1.change_profile("xyz", "F", addr2) == False): 
        print("Unable To Change Profile.")
    
    print("\n")
    # ? print(f"The Type of Addr Class is {type(addr)}.")
    # ? <class.__main__.Address> or something like that.
    customer1.greet()