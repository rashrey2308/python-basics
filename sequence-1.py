'''Anita B sequence challenge 1:
Input a list of strings “str_list” separated by spaces and a character “ch”.
For each unique string in str_list, count the number of occurrences of the character “ch” in that
string and append the string that many times to the answer list and Print the answer list.
Note: It is not necessary that the character “ch” is present in all strings and niqueit is not
necessary that all the strings are unique.'''

str_list=input().split()
str_list1=set(str_list)
str_list=list(str_list1)
ch=input()
#ch=ch[0]
ans_list=[]
count=0
for s in str_list:
    count=0
    count=s.count(ch)
    for i in range(count):
        ans_list.append(s)
print(ans_list)
