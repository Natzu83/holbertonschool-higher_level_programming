class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return self.__str()

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def __str__(self):
        return f"[Square] {self.__width}/{self.__height}"

    def __repr__(self):
        return self.__str()

# Example usage:
square = Square(5)
print(square.area())  # Prints the area: 25
print(str(square))    # Prints the square description: [Square] 5/5
