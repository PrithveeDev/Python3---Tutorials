# ----------------------------------------
# Q. What is OOPs ?
# Ans: Different Way To Write Code.

# ----------------------------------------
# Q. Importance of OOPs ? 
# Ans: Everythin' in python is an Object.

# ----------------------------------------
# Q. Core Concepts of OOPs ? 
# Ans: Classes, Objects, Abstraction, Inheritance, Polymorphism, Encapsulation.

# ----------------------------------------
# Q. What are Classes In Python ? 
# Ans: Class is a BluePrint, That object follows. 

# ----------------------------------------
# Q. What are Two Functions or Types in Classes ? 
# Ans: Class : Data/ Property.
# Ans: Class : Functions/ Behaviors.  
# e.g. For Example: Integer Is of <class 'int'>


# ----------------------------------------
# Q. How to Name a Class & Objects ? 
# Ans: "class NameIsClass"
# Ans: "def class_object_defined():" 
# Imp! Classes Follow ---- (Pascal Case)
# Imp! Variable/Object --- (Snake Case)


# ----------------------------------------
# Q. How To Create Objects ? 
# Ans: Object For "Car" Class could be --- (WagonR, Swift, Fortuner, etc, etc.)
# Ans: Object For "Animal" Class could be --- (Sheep, Dog, Cow, etc, etc.)


# ----------------------------------------
# Q. Why Some Variables/ Object in Python are defined with Some characters (i.e: List1 = [])
# Ans: Those are called "Object LiteraL".
# Ans: list1 = [], also list1 = list(), Because object Literal is easy to implement. 

# ----------------------------------------
# Todo:Let's make A Simple Class --- 
# Imp! Why Do We call Len() function and list.append() a method of a class.
# Ans: Functions inside class will be called methods (of a class).

class ATMClass:
    def __init__(self):
        self.pin = ""
        self.balance = 0.00

        self.menu()
# Imp! What is __init__ : Constructor: 
# Q. Now What is a Constructor ?
# Ans: Constructor is a Special Function/ Method defined in a class,
# >    That Piece of Code Will Be Executed With initialisation of the code.

# e.g. As For example all variables will be defined as soon as the class will be called.
# e.g. Such as ATM_India = ATMClass()

    def check_pin(self):
        try: 
            pin = input("Enter Pin Here:")
            if (pin != self.pin): 
                print("Bad/ incorrect Pin.")
                return False
            else: 
                print("Pin Verified.")
                return True
        except Exception as exe:
            print(f"Bad Input Found {exe}.")


    def menu(self):
        print("Hello, How Would You Like To Proceed?")
        print("1. Enter (1) To Create Pin.")
        print("2. Enter (2) To Deposit.")
        print("3. Enter (3) To Withdraw.")
        print("4. Enter (4) To Check Balance.")
        print("5. Enter (5) To Exit.")
        user_input = input("Enter Here: ")

        if (user_input == '1'):
            self.create_pin()
        elif (user_input == '2'):
            self.deposit_curr()
        elif (user_input == '3'): 
            self.withdraw_curr()
        elif (user_input == '4'): 
            print("Check Balance.")
        elif (user_input == '5'):
            print("Exiting.")
        else:
            print("Bad ----- Request.")

    def create_pin(self):
        pin = input("Enter User Pin:")
        pinVerify = input("Enter User Pin(Again):")

        if (pin != pinVerify):
            print("Both Pins Don't Match, Exiting.")
        else: 
            self.pin = pinVerify
            print("Pin Set Successfully.")

    def deposit_curr(self):
        if (self.check_pin() == True): 
            try: 
                deposit_Amt = int(input("Enter Deposit Amount."))
            except Exception as exe:
                print(f"Exeption occured, Bad, Data Entered: {exe}.")
            else: 
                self.balance += deposit_Amt
                print(f"Deposit Success, Updated Balance is {self.balance}.")

    def withdraw_curr(self): 
        if (self.check_pin() == True): 
            try:
                withdraw_Amt = int(input("Enter Withdraw Amount:"))
            except Exception as exe: 
                print(f"Exeption occured, Bad, Data Entered: {exe}.")
            else:
                if (withdraw_Amt < 0): 
                    print("Value Less Than 0 (zero).")
                else:
                    if (self.balance < withdraw_Amt): 
                        print("Balance Low.")
                    else:
                        self.balance -= withdraw_Amt
                        print(f"Withdrawal Success, Updated Balance {self.balance}.") 


# Q. What is The use of Constructor ? 
# Q. What is Constructor ? 
# Ans: User Doesn't have Control to Constructor.
# Ans: Automatically triggers At Specific Times.
# e.g. Examples: Connecting to GPS, Connect to Internet, Database Connectivity, etc.


# Imp! What is Self ? 
# Ans: "Self" is The object Itself. (You may Ask How? Lemme Explain Then - Refer Below Code.)

class Sample_CLs:
    def __init__(self):
        print(id(self))

# Ans: That Means The Id of "Self" is  == Id of "class Object"
# > obj1 = Sample_CLs()
# > id(obj1) == id(self),
# Imp! That means "Self is -> Object of a Class (i.e. : obj1)".


if __name__ == "__main__":
    Statebank = ATMClass()
    
