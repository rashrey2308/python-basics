'''def reverse(n):
    r=0
    while(n!=0):
        d=n%10
        r=r*10+d
        n=n//10
    return r

print(reverse(int(input("Enter a no. ")))) '''

'''import math
n=int(input("Enter a no. "))
print(int(math.sqrt(n)))'''

i=1
while i<5:
    if i==6:
        break
    print(i, end = " ")
    i=i+1
else:
    print("Else")
