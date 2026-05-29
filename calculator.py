import math
from colorama import Fore, Style, init
init()
FILENAME ="history.txt"
def calculate(num1, op, num2):
    if op == "+":
        return (num1 + num2)
    elif op == "-":
        return (num1 - num2)
    elif op == "*":
        return (num1 * num2 )
    elif op == "/":
        if num2 !=0:
            return(num1/num2)
        else:
            return("Error: can't divide by zero")
    elif op == "**":
        return (num1 ** num2)
    elif op == "%":
        return (num1 % num2)
    elif op == "sqrt":
        return math.sqrt(num1)
    else:
        return("Invalid operator")
history = []
while True:
    try:
        num1 = float(input(Fore.GREEN + "Enter first number: "))
        op = input(Fore.WHITE + "Enter operator (+, -, *, /, **, %):")
        if op == "sqrt":
            result = calculate(num1, op, 0)
        else:
            num2 = float(input(Fore.GREEN + "Enter second number: "))
            result = calculate(num1, op, num2)
        print(Fore.MAGENTA +"Result:", result)
        if op == "sqrt":
            entry = (f"sqrt({num1}) = {result}")
        else:
            entry = (f"{num1} {op} {num2} = {result}")
        history.append(entry)
        with open(FILENAME, "a") as file:
            file.write(entry + "\n")
        
    except:
        print(Fore.RED +"Invalid input! Please enter number!!!!")
    show = input("Do you want to see history? (yes/no): ")
    if show.lower()=="yes":
        print("\n=== History ===")
        for item in history:
            print(item)
    again = input("Do you want another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("Goodbye!!!")
        break