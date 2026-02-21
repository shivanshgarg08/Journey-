#Type Casting In Python

s = "10"
n = int(s)

print(n)
print(type(n))

a = "1"
b = int(a)
print(type(b))

age = 21
s2 = str(age)
print(type(s2))

li = [1 , 2, 3]
d = {'Key' : 'Value'}
bool = True 
print(type(li))
print(type(d))
print(type(bool))

word = "No of Characters"
length = len(word)
print(length)

#Python Operators

import keyword
print(keyword.kwlist)


# Python Data Types 
x = 50  # int
x = 60.5  # float
x = "Hello World"  # string
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
print(x)

#Numeric Data Types 

a = 10 
print(type(a))
b = 10.00
print(type(b))

c = a + 1j
print(type(c))

#Sequential Data Types
a  = ['geekkyy' , 'Vans' , 'lalala' ,'maguire'] #List
print(type(a))
#Accessing Elements from mutable list 
print("Accessing Elements from list")
print(a[0]) # Accessed Element from the list a at indexing 0 = geeky
print(a[1]) # Accessed Element from the list a at indexing 1 = Vans 

# Accessing Elements in list using negative indexing 

print(a[-1])  # Accessed maguire element in list a at indexing -1
print(a[-2])
