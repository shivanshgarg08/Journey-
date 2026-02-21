# Conditional Statements in python
#If - conditional statement 

age = int(input())

if age >= 20:
    print('Eligible to vote')

else :
    print('Not eligible to vote')    

# Short Hand If-Else

marks = float(input())
res = "Pass" if marks>= 50 else "Fail"
print(f"result: {res}")

#Elif Statements
agee = int(input( ))

if agee < 18:
    print('minor')
elif agee< 10:
    print('Child')
elif agee> 18:
    print('young')            