#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
def hypotenuse(a1, a2, flag):
    if flag:
        return (a1**2 + a2**2)**0.5
    else:
        return (max(a1, a2)**2 - min(a1,a2)**2)**0.5