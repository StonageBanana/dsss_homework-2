import random


def function_A(min, max):
    """
    Returns a random integer between min and max.
    """
    return random.randint(min, max)


def function_B():
    """
    Returns a random mathematical operator.
    """
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, operator):
    """
    Forms the math problem based on n1, n2, and the operator, 
    and computes the correct answer.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+': 
        answer = n1 + n2
    elif operator == '-': 
        answer = n1 - n2
    else: 
        answer = n1 * n2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3  # number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = function_A(1, 10); 
        n2 = function_A(1, 5);  # max set to 5 for integer compatibility
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        while True:
            try:
                useranswer = int(input("Your answer: "))
                break
            except ValueError:
                print("Oops! Pleasee enter a valid Integer")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
