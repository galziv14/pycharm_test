# calculator

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2


operations = {"+": add, "-": substract, "*": multiply, "/": division}


def calculator():
    num1 = float(input("what is the first number?"))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Choose an operation:")
        num2 = float(input("What is the second number?"))
        calculation = operations[operation]
        answer = calculation(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        choice = input("press y to continue with this number, press n to start over")
        if choice == "y":
            num1 = answer
        if choice == "n":
            should_continue = False
            calculator()


calculator()