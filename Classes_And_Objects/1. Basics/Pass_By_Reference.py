# ------------------------
# Imp! Let's Craft a New Class Called "Customers".

# > A Class For Storing Customer.
class Customer:

    def __init__(self, name, userId, gender):
        self.name = ""
        self.userId = 0
        self.gender = ""

        self.set_name(name)
        self.set_userId(userId)
        self.set_gender(gender)

    def set_name(self, name):
        if (type(name) is str):
            self.name = name
        else:
            print("Bad Value For Name.")

    def set_userId(self, userId):
        if (type(userId) is int): 
            self.userId = userId
        else: 
            print("Bad Value For userId.")

    def set_gender(self, gender):
        if (type(gender) is str):
            if (gender.isalpha): 
                if (len(gender) == 1) and (gender.upper() == "M" or gender == "F"): 
                    self.gender = gender.upper()
                else: 
                    print("Length Greater Than 1. (Allowed M/F).")                    
            else:
                print("The Value is not Alphabetic. (Allowed M/F).") 
        else: 
            print("Bad Value For Gender (Allowed: M/F).")


# > Define A Function That takes in Class. 
def greet_Func(customer): 
    # ? print(id(customer))
    if (customer.gender == "M"): 
        print(f"Hello! {customer.name}. Sir")
        customer.name = "Prithvee Raj Singh"
    elif (customer.gender == "F"):
        print(f"Hello! {customer.name}. Ma'am")
        customer.name = "Akanksha Singh"

# Q. What is Happening Above? You Know what's Happening But Do You Actually..?
# Ans: Hmm, It's taking Object as Input -- Or, shall we call it "Relative Variable".
# >    Hmm, That Means The "Customer" attribute is same as class object.


if __name__ == "__main__":

    Cust1 = Customer(name="Prithvee", userId=1212, gender="M")
    Cust2 = Customer(name="Akanksha", userId=2121, gender="F")
    greet_Func(Cust1)
    greet_Func(Cust2)

    # ? print(id(Cust1))
    # ? print(id(Cust2))
    # Imp! This is to be noted that we're passing the pointer to -- Greet Function.
    # imp! That Tells us that the nature of class's object are "Mutable"

    print(f"Customer Name: {Cust1.name}.")
    print(f"Customer Name: {Cust2.name}.")
    
    # > The above "Print" Statements Tells us how the Objects are Changed.
    # > That Says Class's Object are Mutable Like Lists, Strings.

