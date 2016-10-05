# Nikolei Advani, 10/5/16
import random


def getProblemType():
    """prompts the user for the problem type"""
    problem = input("What kind of problem would you like?")
    return problem


def getMaxNumber():
    """prompts user for the max number for the problem"""
    max_number = int(input("What is the max number you would like?"))
    return max_number


def getRandomNumber(max_number):
    """generates a random number"""
    random_number = random.randint(1, max_number)
    return random_number


def printProblem(problem, num1, num2):
    """prints problem to user"""
    print(num1, problem, num2)


def promptAnswer():
    """prompts user for answer"""
    answer = int(input("What is the answer?"))
    return answer


def correctAnswer(num1, num2, problem):
    """gets the correct answer of the problem"""
    if problem == "*":
        correct = num1*num2
    elif problem == "-":
        correct = num1-num2
    else:
        correct = num1+num2  # any other input results in an addition problem
    return correct


def compareAnswer(answer, correct):
    """tells user if their answer is correct or not"""
    if correct == answer:
        print("That is correct!")
    else:
        print("Oops! that's not right!")


def main():
    problem = getProblemType()
    max_number = getMaxNumber()
    num1 = getRandomNumber(max_number)
    num2 = getRandomNumber(max_number)
    printProblem(problem, num1, num2)
    answer = promptAnswer()
    correct = correctAnswer(num1, num2, problem)
    compareAnswer(answer, correct)

main()
