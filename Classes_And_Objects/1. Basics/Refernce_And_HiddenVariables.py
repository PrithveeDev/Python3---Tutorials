# ----------------------------------------------------
# Q. How to Make a Variable / Method PRivate in a Python Class ?
# Ans: Use __ (Double Underscore) before a vatiable to make it private.
# > Alternatively You could also use __ (Double Underscore) in front of a Method, 
# > To make it private.

import signal
import sys
# Q. Why Import Signal Handler Module? 
# Ans: Because I'm Tired of seeing those warnings When I press "CtrL + C" or "CtrL + z" and have to
# >    See That dumb dirty Message.


class ATMClass:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0.00 
        signal.signal(signal.SIGINT, self.signal_catcher)
        signal.signal(signal.SIGTERM, self.signal_catcher)
        
    # ? For Initialising Signal Catcher Function. (For Removing those Warnings in TerminaL)
    def signal_catcher(self, sig, frame):
        print("Caught SignaL.")
        sys.exit(0)

    def check_pin(self):
        try: 
            pin = input("Enter Pin Here:")
            if (pin != self.__pin): 
                print("Bad/ incorrect Pin.")
                return False
            else: 
                print("Pin Verified.")
                return True
        except Exception as exe:
            print(f"Bad Input Found {exe}.")

    def transaction_mode(self):
        data = self.__menu() 
        return data

    def __menu(self):
        data = True
        print("Hello, How Would You Like To Proceed?")
        print("1. Enter (1) To Create Pin.")
        print("2. Enter (2) To Deposit.")
        print("3. Enter (3) To Withdraw.")
        print("4. Enter (4) To Check Balance.")
        print("5. Enter (5) To Exit.")
        try: 
            user_input = int(input("Enter Here: "))
        except Exception as exe:
            print("Bad Value.")
            data = False

        if (user_input == 1):
            self.create_pin()
        elif (user_input == 2):
            self.deposit_curr()
        elif (user_input == 3): 
            self.withdraw_curr()
        elif (user_input == 4): 
            self.check_balance()
        elif (user_input == 5):
            data = False
        else:
            print("Bad Request.")
            data = False
        return data

    def set_pin(self, newPin): 
        set = False
        if (type(newPin) is not str):
            set = False
            print("Invalid Pin (TypeError -- Not Valid In This Case).")
        else: 
            if (newPin.isdecimal): 
                set = True
            else: 
                set = False
          
        if set == True:
            self.__pin = newPin

    def get_pin(self):
        print(f"Current Pin: {self.__pin}.")

    def create_pin(self):
        if (self.__pin == ""):                
            pin = input("Enter User Pin:")
            pinVerify = input("Enter User Pin(Again):")

            if (pin != pinVerify):
                print("Both Pins Don't Match, Exiting.")
            else: 
                self.set_pin(newPin=pin)
                print("Pin Set Successfully.")
        else: 
            print("Pin Already Set.")

    def deposit_curr(self):
        if (self.check_pin() == True): 
            try: 
                deposit_Amt = int(input("Enter Deposit Amount."))
            except Exception as exe:
                print(f"Exeption occured, Bad, Data Entered: {exe}.")
            else: 
                self.__balance += deposit_Amt
                print(f"Deposit Success, Updated Balance is {self.__balance}.")

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
                    if (self.__balance < withdraw_Amt): 
                        print("Balance Low.")
                    else:
                        self.__balance -= withdraw_Amt
                        print(f"Withdrawal Success, Updated Balance {self.__balance}.") 

    def check_balance(self):
        print(f"Current Balance is {self.__balance}.")


if __name__ == "__main__":
    Statebank = ATMClass() 

    # Q. What is "Reference Variable" ?
    # Ans: Let's Say -- We Defined a Variable Called "Statebank" that we call an
    # >    Object to the class. 
    # ?    But, Technically Speaking it is not a Object. It's a "Reference Variable"
    # ?    That Stores The Reference of The ATMClass() otherwise it'll be lost.. in
    # ?    Memories...

    data = True
    while True: 
        print("\n")
        data = Statebank.transaction_mode()
        
        # > Note For Usage Later On. 
        # ? print("Pin Currently is: ", end='')
        # ? Statebank.get_pin()
        # ? Statebank.__pin = "1233"
        # ? Statebank.__balance = 1200 
        # ? print(f"\nPin Is Accessable {Statebank.__pin}. But It's Not the same Variable as What we Defined.")
        # ? print(f"Balance is Accessable {Statebank.__balance}. But It's Not the same Variable as What we Defined.\n")
        
        if (data == False): 
            break
    print("Exiting.... ")


# Q. What Exactly Happened Here ?
# Ans: the __ variablss are not normally Accessable.
# Ans: But, It's actually accessable at _ATMClass__balance or _ATMClass__pin.


# Q. Why They're not completely hidden ?
# Ans: Because, Python is made for adults. And don't hide it from fellow programmers. (That's Just PersonaL Problem.)
# > If you wish to hide something from fellow/ Junior Programmers then there's no such way to do so. 
