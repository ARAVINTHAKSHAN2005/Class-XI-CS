# Palindrome checker for strings 
str = str(input("enter the string :"))
l = len(str)
a = 0 
m = 1/2
i = 0 
j = l-1
while i <m:
    if str[i]!= str[j]:
        a = a +1 
        break 
    else:
        i = i +1 
        j = j -1 
if a == 1 :
    print("String is not a palindrome")
else: 
    print("Palindrome")  

 
# program counts number of 2 letter words, and number of lowercase ad uppercase alphabets
str = input("Enter the string: ")
ctr = 0 
lst = list(str.split())
l = len(lst)
for i in range(0,l):
    a = lst[i]
    b = len(a)
    if b ==2:
        ctr = ctr +1 
    
print("number of 2 letter words is = ", ctr )
i = 0 
lc = 0 
uc = 0 
for i in str:
    if (i.islower()):
        lc = lc +1 
    if (i.isupper()):
        uc = uc + 1 
print("No of lowercase is ", lc)
print("No of uppercase is ", uc)