from sympy import *
exit = 0
while exit == 0:
    problem = input("Give a fraction or X to exit: ")
    if problem == "x": exit = 1
    else: 
        answer = N(parse_expr(problem))
        print("%s = %.4f" % (problem, answer))