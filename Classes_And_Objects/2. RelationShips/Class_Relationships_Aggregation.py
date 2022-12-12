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
        if (type(name) is str):
            self.name = name 
        else:
            print("Invalid Name Value.")

    def set_gender(self, gender): 
        set = False 
        if (type(gender) == str):
            if (len(gender) == 1):
                if (gender.upper() == "M" or gender.upper() == "F"):
                    self.gender = gender
                    set = True

        if (set == False):
            print("bad Value for Gender Field (Enter only M/F).")

    def set_address(self, addr):
        self.addr = addr

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
        if (type(city) is str):
            self.city = city 
        else:
            print("Invalid City Value.")
            return False
    
    def set_state(self, state):
        if (type(state) is str):
            self.state = state 
        else:
            print("Invalid State Value")
            return False

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
        data = self.set_city(new_city)
        if (data != False):
            data = self.set_state(new_state)
            
            if (data != False):
                data = self.set_pincode(new_pin)
        
        if data == False: 
            return False


if __name__ == "__main__":
    addr = Address("Ahmedabad", "Gujarat", 201206)
    customer1 = Customer("Prithvee", "M", addr)

    customer1.greet()
    if (customer1.addr.change_address(1212, "Gujarat", 370201) == False):
        print("Unable To Change Address.")
    
    print("\n")
    customer1.greet()