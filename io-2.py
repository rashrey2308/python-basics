n=int(input())
if(n<0 or n>10000):
    exit()
else:
    l=[]
    if n==0:
        print(0)
    else:
        while n!=0:
            l.append(n%10)
            n=n//10
        for i in l[::-1]:
            print(i)
'''def reverse(num):
    reverse_num=0
    no_of_digits=0
    while num!=0:
        reverse_num=reverse_num*10 + num%10
        num//=10
        no_of_digits+=1
    return reverse_num,no_of_digits
def print_num(num):
    num,no_of_digits=reverse(num)
    reversed_no_of_digits=0
    while num!=0:
        print(num%10)
        num//=10
        reversed_no_of_digits+=1
    for _ in  range(no_of_digits-reversed_no_of_digits):
        print(0)
print_num(1000)'''            
