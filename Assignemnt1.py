"""
Assignemnt 1: Simple Programs 
"""

#1. Function Swaps values of two varaibles 
def swapvalues(a,b):
    a,b = b,a 
    print(a,b)

#Example 
val1 = 17 
val2 = 21
swapvalues(val1,val2)

#2. Function that computes Simple Interest 
def simpleinterest(p,r,t):
    #Enter principal, rate, time ( rate in numerical not percentage)
    interest = (p*r*t)/100 
    print(interest)

#Example
simpleinterest(100,5,2)

#3. Python Function to convert Celcius to farenheit 
def celtofaf(num):
    num = int(num)
    f = (num*9/5) + 32
    print(f"{f} F")
    
#Example 
celtofaf(87)

#4. Python Fucnction to calulate average marks 
def average_calc(*args):
    total = sum(args)
    count = len(args)
    average = total/count 
    print(average)

#Example
average_calc(50,70,80)