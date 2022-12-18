import csv 

# Imp!  I'm importing module "csv" because -- we'll try to develop a new 
# !     example of @Static Methods. 

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

    # Q.    What is Class Method "@classmethod" ?
    # Ans:  The decorator "@classmethod" is used when, the class variables are required to be 
    # >     Accessed and Changed.
    
    @classmethod
    def init_object_using_csv(cls, csv_file):
        
        with open(csv_file, 'r') as fiLe:
            reader = csv.DictReader(fiLe)   
            items = list(reader)

        for item in items: 
            print(item)
            names = str(item.get('name'))
            price = float(item.get('price'))
            quant = int(item.get('quantity'))
            Grocery_Updated(names, price, quant)
            


# Imp! Main Function Here.
if __name__ == "__main__":

    Grocery_Updated.init_object_using_csv("1. methods.csv")