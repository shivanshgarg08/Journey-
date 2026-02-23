#   Creating calculator from scratch using if/else statements then using mdodularity and functions

x = float(input("Enter the first number:  " ))
y = float(input("Enter the second number:  " ))
def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)

op = input("Enter the operation to perform *,/,+,- :  ")

if op == "+":
    print("Result : ",add(x,y))
elif op == "-":
    print("Result : ",sub(x,y))
elif op == "*":
    print("Result:  ",mul())
elif op == "/":
    if y == 0:
        print("Cannot divide by zero ❌")
    else:
        print("Result",div(x,y))

def hello():
    return "Hi"

print(hello)
print(hello())            
    
