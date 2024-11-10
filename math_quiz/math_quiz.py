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


def function_C(n1, n2, o):
    """
    Forms the math problem based on n1, n2, and the operator, 
    and computes the correct answer.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': 
        a = n1 + n2
    elif o == '-': 
        a = n1 - n2
    else: 
        a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    total_questions = 3  # number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = function_A(1, 10); 
        n2 = function_A(1, 5);  # max set to 5 for integer compatibility
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
