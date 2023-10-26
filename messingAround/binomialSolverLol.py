import os
import sympy
from sympy import sympify
import pyperclip

os.system("clear")
x = sympy.Symbol('x')
expr_str = input("Problem: ")
expr = sympify(expr_str)
simplified_expr = sympy.expand(expr)

pyperclip.copy(str(simplified_expr))
print(str(simplified_expr))
print("Answer copied!")
