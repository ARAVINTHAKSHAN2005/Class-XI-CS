# Printing the pattern 
i = 1 
ch1 = 'C'
n = int(input("enter the value of n :"))
while i <n:
    j = 1 
    ch = ch1 
    while j <=n+1-i:
        print(ch,end = " ")
        ch = chr(ord(ch)+2)
        j = j +1 
    print("\n")
    ch1 = chr(ord(ch1)+1)
    i = i +1 
    

# Prime factor finder
i = 1 
n = int(input("Enter n: "))
while i <= n:
    k = 0 
    if n%i==0:
        j = 1 
        while j <=i:
            if i%j ==0:
                k = k + 1
            j = j + 1 
        if k == 2 :
            print(f"{i} is a prime factor")
        i = i + 1 
                
       

        

        