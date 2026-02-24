#Functions practice exerecise 

def square(x):
    return x*x
print(square(5))

#Now to get the user input to enter the number and we get the squared output

def sq(a):
    return a*a
num= int(input("Enter the number: "))
print(sq(num))
y = sq(5) + 10 # Usage of return gives actual value and can be used like this autmaticall add 10 to return value
print(y)

#Exercise 2 - Multiparameter

def maxof2(a,b):
    if a>b:
        return a
    else:
        return b
    
num1,num2 = map(int,input("Enter two numbers: ").split())      
print(maxof2(num1,num2))        


#Exercise 3 Default Argument
def_name = input("Enter the name")
def greet(x):
    
    
