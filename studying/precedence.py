import random
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

operators = ['+', '-', '*', '/', '%', '**', '==', '!=', '<', '<=', '>', '>=', 'and', 'or', 'not', '&', '|', '^', '<<', '>>', '>>>']
operator_counts = {op: [0, 0] for op in operators}

def generate_problem():
    """Generates a random operator precedence problem of length 2 to 5"""
    length = random.randint(2, 5)
    operands = [str(random.randint(0, 9)) for _ in range(length)]
    operators = [random.choice(operators) for _ in range(length - 1)]
    problem = ' '.join([f"{operands[i]} {operators[i]}" for i in range(length-1)] + [operands[-1]])
    return problem

def evaluate(problem):
    """Evaluates a given operator precedence problem"""
    return eval(problem)

def submit_answer(answer_label, score_label):
    """Function to submit the user's answer"""
    global operator_counts
    answer = answer_label.get()
    try:
        answer = float(answer)
        if answer == evaluate(problem):
            messagebox.showinfo("Result", "Correct!")
            operator_counts[operator][0] += 1
        else:
            messagebox.showerror("Result", f"Incorrect. The correct answer was {evaluate(problem)}.")
            operator_counts[operator][1] += 1
    except ValueError:
        messagebox.showerror("Error", "Invalid answer. Please enter a number.")
    answer_label.delete(0, END)
    update_score(score_label)

def update_score(score_label):
    """Function to update the user's score"""
    global operator_counts
    total_correct = sum([count[0] for count in operator_counts.values()])
    total_questions = sum([count[0] + count[1] for count in operator_counts.values()])
    score_label.config(text=f"Score: {total_correct}/{total_questions}")

def show_results():
    """Function to show the results in a pie chart"""
    global operator_counts
    labels = []
    correct_counts = []
    incorrect_counts = []
    for operator in operators:
        if operator_counts[operator][0] + operator_counts[operator][1] > 0:
            labels.append(operator)
            correct_counts.append(operator_counts[operator][0])
            incorrect_counts.append(operator_counts[operator][1])
    fig, ax = plt.subplots()
    ax.pie(correct_counts, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title("Accuracy by Operator")
    plt.show()

def main():
    """Main function"""
    root = Tk()
    root.title("Operator Precedence Quiz")
    problem_label = Label(root, text="")
    problem_label.pack(pady=10)
    answer_label = Entry(root)
    answer_label.pack(pady=5)
    submit_button = Button(root, text="Submit", command=lambda: submit_answer(answer_label, score_label))
    submit_button.pack(pady=5)
    score_label = Label(root, text="")
    score_label.pack(pady=10)
    show_results_button = Button(root, text="Show Results", command=show_results)
    show_results_button.pack(pady=5)
    problem = generate_problem()
    problem_label.config(text=f"What is the result of {problem}?")
    update_score(score_label)
    root.mainloop()

if __name__ == '__main__':
    main()
