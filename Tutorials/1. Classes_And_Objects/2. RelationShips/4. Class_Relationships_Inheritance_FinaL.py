# --------------------
# > H'mm Let's see the final "Most Complete" Type of Inheritance.


class Phone:
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
        if (Phone.Initiated == True):
            return f"The Phone {self.brand} {self.name} has a Camera of {self.camera} with a Operating System of {self.os}, Price: {self.price} /-"


if __name__ == "__main__":

    device1 = Phone("Apple", "IPhone 13 Pro", 119990, "IoS 16.1", "50 MpX")
    print(device1.tell_me_the_specs())