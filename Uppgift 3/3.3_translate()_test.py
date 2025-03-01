## this file is a test/demonstration of the function translate(), which is used in uppgift 3.3.py 
from math import *
import readline

def translate(txt: str, var:str) -> str: ## translates expression so that eval() can compute expression
    txt = txt.replace(" ", "") ## ensures there are no spaces
    txt = txt.replace("^","**") # replaces ^ to **
    expression = list(txt) #converts str to list, easier to work with

    def insert_multiplication(expression): ## inserts "*" between characters
        constant = {"0","1","2","3","4","5","6","7","8","9"}
        signs = {"+","-","*","/","^",")","("}
        counter = 1
        while counter < len(expression):
            element = expression[counter]
            element_before = expression[counter-1]

            if element == "(" and (element_before in constant or element_before == var): #e.g. turns 4(1+1) to 4*(1+1)
                expression.insert(counter,"*")
                continue
            if element == "(" and element_before == ")": # e.g turns (x^2+1)(2+x) to (x^2+1)*(2+x)
                expression.insert(counter,"*")
                continue
            if element == var and (element_before in constant or element_before == ")"): #e.g. turns 3x to 3*x
                expression.insert(counter,"*")
                continue
            if element in constant and (element_before == var or element_before == ")"): #e.g. turns x4 to x*4
                expression.insert(counter,"*")
                continue
            if (element not in constant and element not in signs and element != var) and (element_before in constant or element_before == var): #e.g. turns 3sqrt(x) to 3*sqrt(x)
                expression.insert(counter,"*")
                continue
            counter += 1 # counter goes only up if every check has been passed
        result = "".join(expression) # joins back list into string
        return result
    
    return insert_multiplication(expression)
test1 = "5x^2"
test2 = "(x+1)(x-1)"
test3 = "x^2 + 2^(3+1)"
test4 = "(a^2-1)^2 - ((2a-1)a)4"
test5 = "2^(x+1)"
test6 = "3sqrt(x) + 5tan(2x)-sin(x)"

print(f"Test 1: {translate(test1,"x")}") # return 5*x**2
print(f"Test 2: {translate(test2,"x")}") # return (x+1)*(x-1)
print(f"Test 3: {translate(test3,"x")}") # return x**2+2**(3+1)
print(f"Test 4: {translate(test4,"a")}") # return (a**2-1)**2-((2*a-1)*a)*4
print(f"Test 5: {translate(test5,"x")}") # return 2**(x+1)
print(f"Test 6: {translate(test6,"x")}") # return 3*sqrt(x)+5*tan(2*x)-sin(x)
