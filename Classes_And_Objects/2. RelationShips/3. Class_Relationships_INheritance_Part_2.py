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

    def return_device(self):
        print("Returning A Phone.")


class Smart_Phone(Phone):

    def buy_device(self):
        print("Buying A Smartphone.")
        


# --------------- SmartPhone/ Phone (End)---------------


if __name__ == "__main__":

    c1 = Child(12, 13)
    # ? print(f"Child Val is ({c1.get_val()}) and Child Num is ({c1.get_num()})")
    # Imp! This Above "Print()" Statement will give an error since, then

