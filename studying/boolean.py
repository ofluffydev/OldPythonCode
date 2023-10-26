import random

def generate_boolean_question():
    ops = ["<", "<=", ">", ">=", "==", "!="]
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(1, 100)
    a = random.choice([True, False])
    b = random.choice([True, False])
    op1 = random.choice(["and", "or"])
    op2 = random.choice(ops)
    op3 = random.choice(ops)
    question = f"What is the value of ({a} {op1} {b}) {op2} (x {op3} y) and (y != z) and (x {op2} z) and (not b)"
    answer = eval(question.replace("and", "and").replace("or", "or").replace("not", "not").replace("!= True", "is not True").replace("== True", "is True"))
    return (question, answer)

while True:
    question, answer = generate_boolean_question()
    user_answer = input(question + " ").lower().strip()
    if user_answer == str(answer).lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {answer}.")
    continue_playing = input("Do you want to continue? (y/n)").lower().startswith("y")
    if not continue_playing:
        break