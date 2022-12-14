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
    pass
        

# > Main Function.

if __name__ == "__main__":

    Tutor1 = Tutor()

    # ? Tutor1.register()
    # ? Tutor1.login()
    # ? Tutor1.make_video()
    # ? Tutor1.answer()

    Phone1 = Phone("Rs.19,999/-", "Xiaomi Redmi Note 11", "48 Mega Piels")
    # ? Phone1.tell_me_about()

    Smart_Phone1 = Smart_Phone("Rs.29,999/-", "Xiaomi MI 11 Ultra 5G", "200 Mega Piels")
    Smart_Phone1.tell_me_about()




    