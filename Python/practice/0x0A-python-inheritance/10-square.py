Rectangle=__import__("9-rectangle").Rectangle

class Square(Rectangle):
    def __init__(self,size):
        self.integer_validator("Size",size)
        self.__size = size

        super.__init__(size,size)


    def area(self):
       return self.__size**2