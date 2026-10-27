class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return f"{self._width} cm"
    @property
    def height(self):
        return f"{self._height} cm"
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be a positive value.")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be a positive value.")

rectangle = Rectangle(float(input("Enter the value of width: ")), float(input("Enter the value of height: ")))
print(f"Width: {rectangle.width}", f"Height: {rectangle.height}")

# How does using @property make your code easier to read compared to using traditional get_ and set_ methods?
# Using the @property decorator in Python allows for more concise and organized code compared to traditional getter and setter methods, allowing us to easily access and modify existing attributes instead of using roundabout ways.