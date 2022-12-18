# ----------------------------
# Imp! Static Variable Type Modifier, and Methods in A Class.

import signal
import sys
# Q. Why Import Signal Handler Module? 
# Ans: Because I'm Tired of seeing those warnings When I press "CtrL + C" or "CtrL + z" and have to
# >    See That dumb dirty Message.


class ATMClass:

    # ? Counter_SrNo = 0, Say We, Want to Hide this...
    __Counter_SrNo = 0
    
    # Q. Why Defining A Static Variable Here?
    # Ans: Because, We need To define Static Variables Outside the Constructor or Any Other
    # >    Methods of The Class.

    def __init__(self):
        self.__pin = ""
        self.__balance = 0.00 
        
        # Imp! See, We've Implemented A Counter Serial number. 
        # Imp! We Use it During Something Static and That Remains same. (IFSCCode, Name of Bank, Etc.)
        self.Counter_SrNo = ATMClass.__Counter_SrNo
        ATMClass.__Counter_SrNo += 1

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
        return self.__balance


    # Q. What is "@staticmethod" ?
    # Ans: Static Methods Are Type Modifiers For The Class's Methods.
    # >    That tells the Class that we don't need "Self" for accesing 
    # >    THese methods. 

    @staticmethod
    def set_counter(counter_Val): 
        if (type(counter_Val) is int):
            ATMClass.__Counter_SrNo = counter_Val
            print("Counter Set Sucessfully.")
        else: 
            print("Invalid Value For Counter.")

    @staticmethod
    def get_counter():
        print(f"The Value of Counter is {ATMClass.__Counter_SrNo}.")
        return ATMClass.__Counter_SrNo


if __name__ == "__main__":
    Statebank = ATMClass() 
    
    data = True
    while True: 
        print("\n")
        data = Statebank.transaction_mode()
            
        if (data == False): 
            break
    print("Exiting.... ")
