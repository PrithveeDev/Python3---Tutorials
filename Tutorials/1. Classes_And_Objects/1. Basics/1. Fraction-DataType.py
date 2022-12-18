
# Imp! Python Doesn't handle Fraction itself
# > So What we'll do is create A Class For Handling Faction 
# > Using Classes.

class Fraction:
    def __init__(self, nume, deno):
        self.num = nume         # Imp! This is Called an Instance Variable. 
        self.den = deno         # Imp! These are Used when -- we need to define properties of an object. 

# Q. What is This __str__ function/ magic Method ? 
# Ans: THis is a Magic Method That'll Automatically be called. Whenever, we "print (print(class_object_1))" our Class's 
# > Object Using Print. 
    def __str__(self): 
        return f"{self.num}/{self.den}"

# Q. What is This __add__ function/ magic Method ? 
# Ans: THis is a Magic Method That'll Automatically be called. Whenever, we try to "Addition ( + )" our Class's 
# > Objects.
    def __add__(self, other): 
        tNum = self.num * other.den + other.num * self.den
        tDen = self.den * other.den
        return f"{tNum}/{tDen}"

# Q. What is This __sub__ function/ magic Method ? 
# Ans: THis is a Magic Method That'll Automatically be called. Whenever, we try to "Subtraction ( - )" our Class's 
# > Objects.
    def __sub__(self, other):
        tNum = self.num * other.den - other.num * self.den
        tDen = self.den * other.den
        return f"{tNum}/{tDen}"        

# Q. What is This __mul__ function/ magic Method ? 
# Ans: THis is a Magic Method That'll Automatically be called. Whenever, we try to "Multiply (x)" our Class's 
# > Objects.
    def __mul__(self, other):
        tNum = self.num * other.num
        tDen = self.den * other.den 
        return f"{tNum}/{tDen}"

# Q. What is This __truediv__ function/ magic Method ? 
# Ans: THis is a Magic Method That'll Automatically be called. Whenever, we try to "Divide (/)" our Class's 
# > Objects.
    def __truediv__(self, other):
        tNUm = self.num * other.den
        tDen = self.den * other.num
        return f"{tNUm}/{tDen}"

if __name__ == "__main__":
    x = Fraction(4, 5)
    y = Fraction(5, 6)
    print(f"The Addition is {x + y}.")
    print(f"The Addition is {x - y}.")
    print(f"The Addition is {x * y}.")
    print(f"The Addition is {x / y}.")
    


# Q. List Down all The Magic methods that you've seen into this file for future reference for you/ other people. 
# Ans:

# ? Init and Destructors
# > __init__(self, other)   : Get's Called By __new__.
# > __new__(cls, other)     : Get's Called in an Object Initialisation. 
# > __del__(self)           : Destructor.

# ? Operators -- (Comparision Operators)
# > __lt__(self, other)     : gets invoked when, 
# > __le__(self, other)     : gets invoked when, 
# > __eq__(self, other)     : gets invoked when, 
# > __ne__(self, other)     : gets invoked when, 
# > __ge__(self, other)     : gets invoked when, 

# ? Operators -- (Arithmetic Operators)
# > __add__(self, other)            : gets invoked when, operator called is (Addition, +)
# > __sub__(self, other)            : gets invoked when, operator called is (Subtraction, -)
# > __mul__(self, other)            : gets invoked when, operator called is (Multiplication, *)
# > __mod__(self, other)            : gets invoked when, operator called is (Modulo, %)
# > __pow__(self, other[, modulo])  : gets invoked when, operator called is (Power, **)
# > __floordiv__(self, other)       : gets invoked when, operator called is (FloorDiv, //)
# > __truediv__(self, other)        : gets invoked when, operator called is (TrueDiv, /)

# ? Unary Operators (Magic methods)
# > __pos__(self)       : get invoked when, operator called is (Unary Positive, +)
# > __neg__(self)       : get invoked when, operator called is (Unary Negative, -)
# > __invert__(self)    : get invoked when, operator called is (Unary Inverse, ~)

# > __abs__(self)       : get invoked when, operator called is (Built-in Abs-, abs())
# > __round__(self, n)  : get invoked when, operator called is (Built-in round())
# > __ceil__(self)      : get invoked when, operator called is (Built-in math.ceil())
# > __trunc__(self)     : get invoked when, operator called is (Built-in math.trunc())
# > __floor__(self)     : get invoked when, operator called is (Built-in math.floor())

# ? Operators -- (Augmented Assignment)
# > __iadd__(self, other)       : get invoked when, operator called is (+=)
# > __isub__(self, other)       : get invoked when, operator called is (-=)
# > __imul__(self, other)       : get invoked when, operator called is (*=)
# > __idiv__(self, other)	    : get invoked when, operator called is (/=)
# > __ifloordiv__(self, other)  : get invoked when, operator called is (//=)
# > __itruediv__(self, other)   : get invoked when, operator called is (True Division)
# > __imod__(self, other)       : get invoked when, operator called is (%=)
# > __ipow__(self, other)	    : get invoked when, operator called is (**=)

# > __iand__(self, other)       : get invoked when, operator called is (&=)
# > __ixor__(self, other)       : get invoked when, operator called is (^=)
# > __ior__(self, other)        : get invoked when, operator called is (|=)
# > __ilshift__(self, other)    : get invoked when, operator called is (<<=)
# > __irshift__(self, other)    : get invoked when, operater called is (>>=)


# ? Operators -- (Type Convesion)
# > __int__(self)       : get invoked when, operator called is (Built-in int())
# > __oct__(self)       : get invoked when, operator called is (Built-in oct())
# > __hex__(self)       : get invoked when, operator called is (Built-in hex())
# > __index__(self)     : get invoked when, operator called is (Built-in slice Expression)
# > __trunc__(self)     : get invoked when, operator called is (Built-in math.trunc())
# > __float__(self)     : get invoked when, operator called is (Built-in float())
# > __complex__(self)   : get invoked when, operator called is (Built-in complex())



# ? Operators -- (Strings)
# > __str__(self)               : get invoked when, operator called is (Built-in str())
# > __unicode__(self)           : get invoked when, operator called is (Built-in unicode())
# > __format__(self, formatstr) : get invoked when, operator called is (str.format() or f"")
# > __sizeof__(self)            : get invoked when, operator called is (Built-in sys.getsizeof() -- to return size of object)
# > __repr__(self)              : get invoked when, operator called is (Built-in repr() ----------- (Machine Readable Repr. of type))
# > __hash__(self)              : get invoked when, operator called is (Built-in hash() ----------- to return a integer)
# > __nonzero__(self)           : get invoked when, operator called is (Built-in bool() ----------- to return True/ False)
# > __dir__(self)               : get invoked when, operator called is (Built-in dir() ------------ to return list of implemented class's objects)
