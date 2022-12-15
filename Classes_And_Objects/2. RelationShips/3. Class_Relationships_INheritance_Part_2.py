# ------------------------------ 
# Imp! So, Let's Have a New --- 



class Parent:
    def __init__(self, num):
        self.__num = num
    
    def get_num(self):
        return self.__num



class Child(Parent):
    
    def show(self):
        print("This is Child Class.")


if __name__ == "__main__":
    num = 12
    son = Child(num)
    print(son.get_num())
    son.show()