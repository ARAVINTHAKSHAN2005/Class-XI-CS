"""
Record Programs 1-4 A.S Aravinthakshan X1 A9 JC 7303
"""

#Program 1 
#Function that converts height in cm to feet and inches 
def height_converter():
    centi = float(input("Please Enter your height in cm :"))
    inches = centi*0.3937
    ft = inches/12
    inches1 = inches%12
    print(f'The users height is {ft} feet and {inches1} inches tall')

#Example 
height_converter()


#Program 2
#Function checks if a number is an Amstrong number 
def amstrong_checker():
    sum = 0 
    num = int(input("Enter your number, to check if it is an Amstrong Number: "))
    n1 = num 
    r1 = n1%10
    sum = sum + (r1**3)
    print(r1)
    n2 = num 
    r2 = (n2//10)%10
    sum = sum + (r2**3)
    print(r2)
    n3 = num 
    r3 = n3//100
    sum = sum + (r3**3)
    print(r3)
    if sum == num:
        print(f"{num} is an Amstrong Number")
    else:
        print(f"{num} is not an Amstrong Number")
#Example
amstrong_checker()

#Program 3 
#Function calculates SI and CI
import math 
def si_ci_calc():
    p = int(input("Enter Principal Amount: "))
    r = int(input("Enter Rate of Interest per annum: "))
    t = int(input("Enter the time period for interest calculation: "))
    si = (p*r*t)/100 
    print(f"The SI is {si}")
    ci = (p*(1+(r/100))**t)-p
    print(f"The CI is {ci}")

#Example
si_ci_calc()

#Program 4 
#Finding Average and Assigning Grade
def average_calc():
    m1 = int(input("Enter marks of Subject 1: "))
    m2 = int(input("Enter marks of Subject 2: "))
    m3 = int(input("Enter marks of Subject 3: "))
    m4 = int(input("Enter marks of Subject 4: "))
    m5 = int(input("Enter marks of Subject 5: "))
    total = m1+m2+m3+m4+m5
    count = 5
    average = total/count 
    return average

def grade_assigner():
    average_marks = average_calc()
    if average_marks >=90 and average_marks <=100:
        grade = "O"
    if average_marks >=80 and average_marks <=89:
        grade = "A"
    if average_marks >=70 and average_marks <=79:
        grade = "B"
    if average_marks >=60 and average_marks <=69:
        grade = "C"
    if average_marks >=50 and average_marks <=59:
        grade = "D"
    if average_marks< 50:
        grade = "E"
    print(f"Marks = {average_marks} \nGrade = {grade}")

#Example 
grade_assigner()