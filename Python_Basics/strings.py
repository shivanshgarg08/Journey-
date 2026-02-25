#Strings depth in python:
s1 = 'gfg' 
s2 = 'shshs'

print(s1)
print(s2)
print(type(s2))
#MultiLine String 
s = ''' fbjnfna
jbfjsbfjbsf
fdsfjsfba'''
print(s)

#Accessing Characters In String 
#Positive indices starts at 0 from left; Negative indices starts at -1 from the right
s3 = "Shivansh Garg"
print(s3[0])  # At 0 index S is printed 
print(s3[4])  #Printed 5th character of the string 
print(s3[-1])  #Used negative indexing  printed last character g at -1
print(s3[-4])

#Strings Slicing: 
#Slicing can be done using specifying starting and ending indexing syntax is [start:end]
print(s3[1:4]) #
print(s3[0:3]) # Starting index to 2 
print(s3[:3]) # From starting index 0 to index 2
print(s3[3:])  #From index 3 to end 
print(s3[::-1]) # It is used to reverse the string

#String Iterations 
s4 = "Python"
for char in s4:
    print(char)

# String Immutability 
s = "Shivansh Garg"
s = "G" + s[1:]   # create new string to update first character 
print(s)

g = "geekybaniya"
g = "G" + g[1:] #Creates new string 
print(g)

h =  "Hello World" 
h2 = h.replace("hello","Helloji")
print(h2)

s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("G", "GeeksforGeeks")  # replace word
print(s1)
print(s2)

i = "Hello World"
i_new = i[:2] + "X" + i[3:]
print(i_new)