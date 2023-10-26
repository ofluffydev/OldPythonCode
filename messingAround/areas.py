import pyperclip as clippy
print("Pick a shape")
print("(1)Trapezoid")
print("(2)Triangle")
print("(3)Parallelogram/Square/Rectangle")
print("(4)Rhombus")
print()
shape = int(input("Choice: "))
if(shape <=4):
    if(shape == 1):
        baseOne = float(input("Base one? "))
        baseTwo = float(input("Base two? "))
        height = float(input("Height? "))
        area = ((baseOne + baseTwo)*0.5)*height
        clippy.copy(str(area))
        print(area)
        print("Area Copied!")
    elif(shape == 2):
        length = float(input("Base? "))
        height = float(input("Height? "))
        area = (length*height)/2
        clippy.copy(str(area))
        print(area)
        print("Area copied!")
    elif(shape == 3):
        base = float(input("Base? "))
        height = float(input("Height? "))
        area = base*height
        clippy.copy(str(area))
        print(area)
        print("Area copied!")
    elif(shape == 4):
        diagonalOne = float(input("Diagonal one? "))
        diagonalTwo = float(input("Diagonal two? "))
        area = (diagonalOne*diagonalTwo)/2
        clippy.copy(str(area))
        print(area)
        print("Area copied!")
else:
    print("Unavaliable shape choice.")

