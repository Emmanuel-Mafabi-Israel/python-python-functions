# GLORY BE TO GOD,
# RUNNING PYTHON CODE, 
# CREATING A PYTHON APPLICATION - PYTHON FUNCTIONS,
# BY ISRAEL MAFABI EMMANUEL

def greet_programmer():
    print("Hello, Programmer!")

def greet(name:str):
    print(f"Hello, {name}!")

def greet_with_default(name:str="Emmanuel"):
    print(f"Hello, {name}!")

def add(num1:int, num2:int):
    return num1 + num2

def halve(number:int) -> float:
    # cheking if the number is an integer
    if number % 1 != 0:
        return 0
    else:
        return number / 2