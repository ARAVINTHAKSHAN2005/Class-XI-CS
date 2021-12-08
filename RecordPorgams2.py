def lcm_hcf_finder(a,b):
    
    if a > b :
        small = a 
    else:
        small = b 
    i = 1
    while i<=small:
    
        if a%i==0 and b%i==0:
            hcf = i
            lcm = (a*b)/hcf
        i += 1        
    
    print(f"the hcf is {hcf}, and the lcm is {lcm}")   


lcm_hcf_finder(92,46)


def root_finder(a,b,c):
    #ax^2 + bx + c
    a = int(a)
    b = int(b)
    c = int(c)

    D =  (b**2 - 4*a*c)
    if D > 0:
        root1 = -1*((D**0.5)+b )/(2*a)
        root2 = ((D**0.5)-b )/(2*a)
        print((root1,root2))

    elif D == 0:
        print("The Roots are real and equal")
        root = -1*((D**0.5)+b )/(2*a) 
        print((root,root))
    else:
        print(" No real roots for given Quadratic Equation, roots are imaginary")

#Example 
#root_finder(1,6,9)

#fibonachi_generator(10)
def fibonachi_generator(n):

    n1 = 0
    n2 = 1 
    print(n1,n2,end=" ")
    i = 2 
    while i<n:
        n3 = n1+n2
        print(n3,end=" ")
        n1,n2=n2,n3
        i += 1 



import math 
def sum_of_series(x,n):
    i = 1 
    sum = 0 
    while i <n:
        fact = 1 
        j = 1 
        while j<=2*i-1:
            fact *=j
            j +=1
        sum = sum +pow(-1,i+1)*(pow(x,2*i-1))/fact
        i = i+1
    print(sum)
    
sum_of_series(1,3)