#Python Functions Walkthrough 
#def function_name(parameters):
#   statements 
#  (body of the statements)
#  return expression  (here return function is  used)

def fun():
    print("Welcome to the python world")

fun()   #Driver code to call fun() function   

def evenodd(x):
    if (x%2 == 0):
        return ('Even')
    else:
        return('Odd')
print(evenodd(33))
print(evenodd(19))    

def add(a,b):  #Parameters value received here like variable placeholder
    print(a+b)  

add(5,3)   #Function called and arguments passed here 

def greet(name):
    print("Hello ", name)

greet(input("Enter Your Name: " ))


def test(a, b):
    print(a, b)

test(10, 20)
test(b=5, a=3)

def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()