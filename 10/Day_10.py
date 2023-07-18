from replit import clear
from art import logo


def addition(num1, num2):
    return (num1 + num2)

def subtraction(num1, num2):
    return (num1 - num2)

def multiplication(num1, num2):
    return (num1 * num2)

def division(num1, num2):
    return (num1 / num2)

operators = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

def oper():
    try:
        print(logo)
        not_finished = True   
        first_num = float(input("What's the first number?\n"))
            
        while not_finished:
            chosen_operator = input('Pick an operation (+ - * /): ')
            second_num = float(input("What's the second number?\n"))
            calculator_function = operators[chosen_operator]
            result = calculator_function(first_num, second_num)
            print(f'{first_num} {chosen_operator} {second_num} = {result}')
                
            if input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: ").lower() == 'y':
                clear()
                print(f'Your first number: {result}')
                first_num = result
            else:
                not_finished = False
                clear()
                oper()
    except:
        print('Invalid input')
oper()