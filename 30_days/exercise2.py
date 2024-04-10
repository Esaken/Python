width = float(input( "Enter the Rectanle's width: "))
height = float(input( "Enter the Rectanle's height: "))

def area():
    return  height * width
    
def perimeter():
    return ((height * 2) + (width*2))


result = print("Area of the rectangle is: ", area())
result = print("Perimeter of the rectangle is: ", perimeter())