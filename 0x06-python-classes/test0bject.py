#!/usr/bin/python3
class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    def getArea(self):
        return (self.__width) * (self.__height)


def main():
    aSquare = Square()

    height = int(input("enter Width: "))
    width = int(input("enter Height: "))

    aSquare.height = height
    aSquare.width = width

    print("Height :", aSquare.height)
    print("Width :", aSquare.width)

    print("The area is :", aSquare.getArea())

main()
