#Area & Perimeter 
shapeChoice = ""

def run():
    global shapeChoice
    print("Pick a shape")
    print("(1)Rectangle")
    print("(2)Square")
    print("(3)Parrallelogram")
    print("(4)Triangle")
    print("(5)Rhombi")
    print("(6)Trapezoid")
    print()
    shapeChoice = int(input("Choice: "))

run()
if(shapeChoice == 1):
    pass
elif(shapeChoice == 2):
    pass
elif(shapeChoice == 3):
    pass
elif(shapeChoice == 4):
    pass
elif(shapeChoice == 5):
    pass
elif(shapeChoice == 6):
    pass
else:
    print("Incorrect choice of: "+str(shapeChoice))
    print("Please try again")
    run()