#1
class String():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = String()
str1.get_String()
str1.print_String()

#2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0 

class Square(Shape):
    def __init__(self,length):

        self.length = length
    

    def get_area(self):
        return self.length**2
S1=Square(4)
print(S1.get_area())

#3
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def get_area(self):
        return self.length**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    
    def get_area(self):
         return self.length * self.width

S1=Square(2)
print(S1.get_area())
R1=Rectangle(2, 3)
print(R1.get_area())
