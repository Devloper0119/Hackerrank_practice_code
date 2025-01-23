'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

'''

n=int(input("Enter Number Weird or Not weird = "))
print(n)
if n % 2 !=0:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not weird")
elif n >= 6 and n <=20:
    print("Weird")
else:
    print("Not Weird")

