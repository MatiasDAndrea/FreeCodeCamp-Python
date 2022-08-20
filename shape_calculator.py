##################################################################
#
#   shape_calculator: object oriented programming to create a 
#                     Rectangle class and a Square class.
#   
#   Class:
#       Rectangle (width,height)
#           methods:
#               -set_width(width): Sets rectangle width.
#               -set_height(height): Sets rectangle height.
#               -get_area: Calculates rectangle Area.
#               -get_perimeter: Calculates rectangle Perimeter.
#               -get_diagonal: Calculates rectangle diagonal.
#               -get_picture:  Obtain rectangle picture.
#               -get_amount_inside(obj): Amount of figures 
#                   that can get inside the created rectangle.
#
#       Square (side) - Inherits from Rectangle
#           methods:
#               -set_width(width): Sets square sides.
#               -set_height(height): Sets square sides.
#               -set_side(side): Sets square sides.
#               -get_area: Calculates square Area.
#               -get_perimeter: Calculates square Perimeter.
#               -get_diagonal: Calculates square diagonal. 
#               -get_picture:  Obtain square picture.
#               -get_amount_inside(obj): Amount of figures 
#                   that can get inside the created square.
#               
####################################################################

class Rectangle:

    def __init__(self,width,height):
        self.width  = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self,changed_width):
        self.width = changed_width

    def set_height(self,changed_height):
        self.height = changed_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height **2) ** 0.5

    def get_picture(self):

        if self.width > 50 or self.height >50:
            return("Too big for picture.")
        else :
            string = f"{'*'*self.width}\n"
            string = string*self.height
            return string

    def get_amount_inside(self,obj):

        foreign_width  = obj.width
        foreign_height = obj.height
        width  = self.width
        height = self.height

        width_times  = width  // foreign_width
        height_times = height // foreign_height

        times = width_times * height_times
        return times


class Square(Rectangle):

    def __init__(self,side):
        self.height = side
        self.width  = side

    def __str__(self):
        return f"Square(side={self.height})"

    def set_side(self,changed_side):
        self.width  = changed_side
        self.height = changed_side

    def set_width(self,changed_width):
        self.width  = changed_width
        self.height = changed_width

    def set_height(self,changed_height):
        self.height = changed_height
        self.width = changed_height


####################
# Tests
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))