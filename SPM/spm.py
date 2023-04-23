from termcolor import colored

def add(a, b):
    print(colored(str(a), "blue") + " + " + colored(str(b), "blue") + " = " + colored(str(a+b), "green"))

def subtract(a, b):
    print(colored(str(a), "blue") + " - " + colored(str(b), "blue") + " = " + colored(str(a-b), "red"))
