#Starting out with the loops with for -loops and while-loops
n = 4
for j in range(0,n):
    print(j)

#For - loop iterate over a sequence structures like list , tuple, sting or range 
# once for each item , allows to execute block of code repeatedly 
# this code print numbers from o to 3 using a for loop that iterates over a range from o to n-1
# where (n=4) - 3-1,2-1,1-1 

#Real world analogy for for-loop is taking attendance in a class
# taking attendance for ex 5 students in class represent in the form of list 
#task is to call each name mark present and stop after takng last name 

students  = ["Aman","Shivansh","Anish","Dhruv","Ishan","SaI"]

for student in students:
    print(student)
    
word = "Hello"

for letter in word:
    print(letter) 

# Iterating over list,tuple ,string  And Dictionary using For loops in python

li = ["shiv","sai","ishan","neha","kapil"]
for names in li:
    print(names)

tup = ("Geeks","for","Geeks")
for x in tup:
    print(x) 

string = "abcd"
for x in string:
    print(x)

d = dict({'x': 123 , "y":456})
for x in d:
    print("%s  %d" % (x, d[x]))

li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])
i = 0
while i < 5:
    i = i + 1 
    print("Geeks for geeks")

# Printing a table of a number using loops 
n = int(input("Enter n: "))
i = 1
while i <= 10:
    print(i,'*',n,"=",i*n)
    i = i + 1        