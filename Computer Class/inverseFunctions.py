def f(x):
    # y = 5x + 3
    return 5*x + 3

def g(x):
    # y = (x - 3) / 5
    return (x-3)/5


number = float(input("Choose a number: "))

gOfFOfX = g(f(number))
fOfGOfX = f(g(number))
FOfX = f(number)
GOfX = g(number)

print()
print("f(g("+str(number)+")) is equal to: "+str(gOfFOfX))
print()
print("g(f("+str(number)+")) is equal to: "+str(fOfGOfX))
print()
print("f("+str(number)+") is equal to: "+str(FOfX))
print()
print("g("+str(number)+") is equal to: "+str(GOfX))

# Replace the function name with "y": y = 3x + 4
# Swap x and y: x = 5y + 3
# Solve for y: y = (x - 3) / 5
# Replace y with the inverse function notation: f^(-1)(x) = (x - 4) / 3