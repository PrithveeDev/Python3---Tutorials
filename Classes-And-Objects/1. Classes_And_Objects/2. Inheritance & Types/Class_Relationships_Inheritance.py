# --------------------------
# Imp! Inheritance In A Nutshell - Tutorial. 


# Q. Why Do we Need "Inheritance" ? First Question is That.
# Ans:  Let's See most study websites/ platform have two - three target audience. One is 
# >     Admin him/herself other than that there's "Instructor" and "Student".

# Imp! Therefore, Student Can Do Login, Register, Take Courses, Review.
# Imp! Whereas, Instructor will do Login, Register, Make Course, Answer


# Q. Principle of Inheritance ? 
# Ans:  What's Yours is Mine(One Inheriting (Child)), 
# >     What's Mine is Not Yours (One Being Inherited (Parent)). 

# Q. What All Do Inherit From the "Parent Class" ?
# Ans:  1.) Data Members (Variables), 2.) Member Functions (Methods) 
# >     3.) Constructors. 

# Imp! Private Members (__number or self.__number) are not inherited.



# --------------------------------------------------
# ? Code 1:
class User: 

    def login(self):
        print("SuccessFully Logged In.")
       
    def register(self):
        print("SuccessFully Registered.")


class Tutor(User):

    def make_video(self): 
        print("Video Created.")
       
    def answer(self):
        print("Question Answered.")

# --------------------------------------------------
# ? Code 2:
class Phone: 
    def __init__(self, price, brand, camera):

        self.set_price(price)
        self.set_brand(brand)
        self.set_camera(camera)
        

    def set_price(self, price): 
        set = False
        if (type(price) is str):
            self.price = price
            set = True
        else:
            print("Unable to set Price.")
        
        return set
    
    def set_brand(self, brand):
        set = False
        if (type(brand) is str):
            self.brand = brand
            set = True
        else:
            print("Unable to set Brand.")
        
        return set
        
    def set_camera(self, camera):
        set = False
        if (type(camera) is str):
            self.camera = camera
            set = True
        else:
            print("Unable to set Camera.")
        
        return set
        
    def tell_me_about(self):
        print(f"The {self.brand} Mobile is quite good, with a price of {self.price}, along with a camera system of {self.camera}.")


    def buy_device(self):
        print("Buying A Phone.")

    def return_device(self):
        print("Returning A Phone.")


class Smart_Phone(Phone):
    
    # Q. If This Function Has Same Name as The Parent Class Name "buy_device"?
    # Q. So, What does happen when you call it ? Does it call local function / Parents Class? 
    # Ans: Hmm, This is Called -- PolyMorphism. (Method Overriding.)

    def buy_device(self):
        print("Buying A Smartphone.")
        

# ------------------------------ 
# Imp! So, Let's Have a New --- 


# ------------------- Parent/ Child (Start)---------------
class Parent:
    def __init__(self, num):
        self.__num = num
    
    def get_num(self):
        return self.__num



class Child(Parent):

    def __init__(self, val, num):
        self.__val = val


    def get_val(self):
        return self.__val
# --------------- Parent/ Child (End)---------------



# --------------- SmartPhone/ Phone (Start)---------------

class Phone: 
    def __init__(self, price, brand, camera):

        self.set_price(price)
        self.set_brand(brand)
        self.set_camera(camera)
        

    def set_price(self, price): 
        set = False
        if (type(price) is str):
            self.price = price
            set = True
        else:
            print("Unable to set Price.")
        
        return set
    
    def set_brand(self, brand):
        set = False
        if (type(brand) is str):
            self.brand = brand
            set = True
        else:
            print("Unable to set Brand.")
        
        return set
        
    def set_camera(self, camera):
        set = False
        if (type(camera) is str):
            self.camera = camera
            set = True
        else:
            print("Unable to set Camera.")
        
        return set
        
    def tell_me_about(self):
        print(f"The {self.brand} Mobile is quite good, with a price of {self.price}, along with a camera system of {self.camera}.")


    def buy_device(self):
        print("Buying A Phone.")


class Smart_Phone(Phone):

    def buy_device(self):
        print("Buying A Smartphone.")
        super().buy_device()

        # Q. What Does "Super.Function()" Do ?
        # Ans:  Hmm, What it actually des -- it wakes up the parent's class with "function()'s" 
        # >     Name. That means "super().buy_device()" will call the parent's function.     
# --------------- SmartPhone/ Phone (End)---------------

# --------------- Phone (Start)---------------
# > H'mm Let's see the final "Most Complete" Type of Inheritance.

class Phone_FinaL:
    Initiated = False
    def __init__(self, brand : str, name : str, price : float, os: str, camera: str):
        try: 
            assert len(camera) > 0,   f"Bad Camera Fed."
            assert len(brand) > 0,  f"Bad Brand Name Fed."
            assert len(name) > 0,   f"Bad Name Fed."
            assert len(os) > 0,   f"Bad Os Value Fed."
            
            assert price > 0,       f"Bad Price Fed."

        except Exception as exe: 
            print(f"Exception Occured During Assertion {exe}.")
        else:
            self.camera = camera
            self.price = price
            self.brand = brand 
            self.name = name
            self.os = os

            # Imp! Checker For Checking if Class is Initialised Or Values Are Invalid.
            Phone.Initiated = True
    
    def tell_me_the_specs(self):
        if (Phone_FinaL.Initiated == True):
            return f"The Phone {self.brand} {self.name} has a Camera of {self.camera} with a Operating System of {self.os}, Price: {self.price} /-"


class Smart_Phone_FinaL(Phone_FinaL):
    def __init__(self, brand: str, name: str, price: float, os: str, camera: str):
        super().__init__(brand, name, price, os, camera)

    def who_are_you(self):
        return f"I'm a Smartphone {self.brand} {self.name}."

# --------------- Phone / Phone (End)---------------



# > Main Function.

if __name__ == "__main__":

    Tutor1 = Tutor()
    Smart_Phone1 = Smart_Phone("Rs.29,999/-", "Xiaomi MI 11 Ultra 5G", "200 Mega Piels")

    print("------------------ User/ Student Classes (Start) ---------- ")
    Tutor1.register()
    Tutor1.login()
    Tutor1.make_video()
    Tutor1.answer()
    print("------------------ User/ Student Classes (End) ---------- ", end= "\n\n")



    print("------------------ Phone/ SmartPhone Classes (Start) ---------- ")
    Smart_Phone1.tell_me_about()
    Smart_Phone1.buy_device()
    print("------------------ User/ Student Classes (End) ---------- ", end="\n\n")



    print("------------------ Child Classes (Start) ---------- ")
    c1 = Child(12, 13)
    # ? print(f"Child Val is ({c1.get_val()}) and Child Num is ({c1.get_num()})")
    # Imp! This Above "Print()" Statement will give an error since, then

    smart_phone = Smart_Phone("Rs. 19,000/-", "Xiaomi Redmi K40 Pro", "48 MegaPixels")
    smart_phone.tell_me_about()
    smart_phone.buy_device()
    print("------------------ Child Classes (End) ---------- ", end="\n\n")


    print("------------------ Phone Class FinaL Classes (Start) ---------- ")
    device1 = Phone_FinaL("Apple", "IPhone 13 Pro", 119990, "IoS 16.1", "50 MpX")
    device2 = Smart_Phone_FinaL("Xiaomi", "MI 13 Pro Ultra", 119999, "MiUi", "200 MegaPixels")
    print(device1.tell_me_the_specs())
    print(device2.tell_me_the_specs())
    print(device2.who_are_you())

    print("------------------ Phone Class FinaL Classes (End) ---------- ", end="\n\n")
