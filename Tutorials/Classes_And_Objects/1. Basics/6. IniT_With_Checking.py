# --------------------------
# ? I've Learning a lot but missed some -- aspects. 
# ? Therefore, Redo.

# Imp! So, Let's Do Init With dataType Checking Instead of Doin' it the long way.


class Grocery:
    # > Setting the Default "quatity" to 1.
    def __init__(self, name, price, quantity = 1):

        # ? Assigning Values To ---- Variables..
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity



class Grocery_Updated:
    """
    This is Updated Function, This is Just Sample Doc String. 
    This surpasses the older Class.
    """
    __pay_rate = 0.8
    # > Setting the Default "quatity" to 1.
    def __init__(self, name: str, price: float, quantity = 1):
        self.legit_user = False
        self.total_price = 0
        self.discounted_price = 0

        # Imp! "Assert" PrincipLe
        # Q. So What Exactly Does "Assert" Do ?
        # Ans:  "Assert" is a keyword that is meant to check some coditional statement.
        # >     If "False" it'LL raise "AssertionError: With Message Attached to Assertion.

        # ? Asserting Statements And Assigning Em' 
        try: 
            assert price > 0, f"Price {price} is not Greater Than Zero."
            assert quantity > 0, f"Quantity {quantity} is not Greater Than Zero."
        except Exception as exe:
            print(f"Excepting {exe} occured While Assigning Values.")
        else:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.legit_user = True

    def calculate_total_price(self):
        if (self.legit_user == True):
            self.total_price = self.price * self.quantity
            return self.total_price
        else: 
            return False

    def apply_discount(self):
        if (self.legit_user == True):
            if (self.total_price == 0):
                self.total_price = self.price * self.quantity
                print(f"Calculating Total.. as {self.total_price}")
            
            self.discounted_price = self.total_price * Grocery_Updated.__pay_rate
            return self.discounted_price

        else: 
            return False


    # > This is Representation magis Method.     
    def __repr__(self):
        return f"Grocery(\"{self.name}\")"
    
# Imp! - Main Function Starts Here.
if __name__ == "__main__":

    object_simple = Grocery("Pringles", "$ 15", 3)
    price_simple = object_simple.calculate_total_price()
    print(f"Total Price For {object_simple.name} for Quantity {object_simple.quantity} is {price_simple}.")
    # To Note-- We've not applied any checking in the class, Therefore, we'll get unexpected 
    # $         Result (100010001000 != Total Cost, Total Cost Shall Be 3000), Therefore we 
    # $         Need a kind of checking datatype.

    object_updated = Grocery_Updated("Washing Powder", "$ 120", -1)
    object_updated.calculate_total_price()
    # To Note-- This is Much Better approach Since We Have A Checking Here.

    print()
    print("The all Variables associated with....")
    print(f"The __dict__ of object_simple is {object_simple.__dict__}.")
    print(f"The __dict__ of object_updated is {object_updated.__dict__}.")
    
    # ? print(end="\n")
    # ? print(f"The __dict__ of Class \"Grocery Updated\" is \n{Grocery_Updated.__dict__}.")
    # ? print(f"The __dict__ of Class \"Grocery\" is {Grocery.__dict__}.")


    print()
    object_final = Grocery_Updated("Miniature Radio", 199, 2)
    discount = object_final.apply_discount()
    print(f"Price After Discount on \"{object_final.name}\" for {object_final.quantity} pieces is {discount}.")

    print(object_final)