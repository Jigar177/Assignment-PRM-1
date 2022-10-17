'''Python Candidates - Question 1

You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.

For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']

Input Format:

At first-line it will have an integer (number of elements inside a list). In the second line, it will have a string.

Output Format:

A single line containing a sorted list.'''

# Ans


list = ['great','hello','hiyo','abc']   

list.sort(key=lambda  l : l[-2])
print(list)





'''  Q2.


﻿Your task is to complete the validate_triangle and validate_rectangle functions for the classes.Hint for validating is given in the

comments of the code. Also you will have to print the following after validation in respective functions:-

1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)

2.Valid Triangle:If the triangle sum property of sides is valid.

3.Valid Rectangle:If 2 side pairs are same and they are input in correct order like l,b,l,b

4.Invalid Rectangle: If Not Valid rectangle as stated above.

Input Format:

The side length of triangle followed by for rectangle in the next line in order.

Output Format:

since object are created in order, so first validate info about triangle will come and than rectangle.

Sample Input 0:

3 4 5

2 4 2 4

Sample Output 0:

Valid Triangle

Valid Rectangle'''


def rectCheckValidity(a, b, c, d):
    if(a == c and b == d) :
        if(a * 2 == b) :
            return True
    return False

a = 2
b = 4
c = 2
d = 4

if rectCheckValidity(a, b, c ,d):
    print("Valid")
else:
    print("Invalid")




def checkValidity(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True       

a = 3
b = 4
c = 5
if checkValidity(a, b, c):
    print("Valid")
else:
    print("Invalid")




   