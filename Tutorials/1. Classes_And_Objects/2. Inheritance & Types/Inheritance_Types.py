# -----------------------
# Imp! Multi-Level Inheritance.

class Product:
    def __init__(self, productId : int):
        try: 
            assert productId > 0,   f"Bad Value For productId."
        except Exception as exe:
            print(f"Exception {exe}.")
        else: 
            self.product_id = productId


class Phone(Product):
    Initiated = False
    def __init__(self, productId : int, brand : str, name : str, price : float, os: str, camera: str):
        super().__init__(productId)
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

    def TellMeAbout(self):
        print(f"The Phone {self.brand} {self.name} is fitted with {self.camera} camera System, and comes with {self.os} system, product-Id {self.product_id}")


class SmartPhone(Phone):
    
    def __init__(self, productId: int, brand: str, name: str, price: float, os: str, camera: str):
        super().__init__(productId, brand, name, price, os, camera)

    def TellMeAbout(self):
        print(f"The SmartPhone {self.brand} {self.name} is fitted with {self.camera} camera System, and comes with {self.os} system, product-Id {self.product_id}")

if __name__ == "__main__":
    print("----------------- Phone (start)---------------")
    device1 = Phone(11901, "Apple", "Iphone 13 Pro", 199999, "IoS 16.1", "50 Mega Pixels")
    device1.TellMeAbout()
    print("----------------- Phone (end)---------------", end="\n\n\n")


    print("----------------- SmartPhone (start)---------------")
    device2 = SmartPhone(19901, "Xiaomi", "Mi 12 Pro Ultra", 23999, "MiUi 14", "200 Mega Pixels")
    device2.TellMeAbout()
    print("----------------- SmartPhone (end)---------------", end="\n\n\n")
