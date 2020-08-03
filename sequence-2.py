'''1.   Calculate how many unique elements in L1.
2.   After looking at the result of first step , print odd elements only.
3.   For string str1 replace “three” with “3” and save all words in some list where  all the character should be capital.
4.   Also explain in your own words that how tuple are immutable(using list L1). (BONUS QUESTION)
#Hint: use tuple(LIST) method to convert L1 into tuple.
'''
l1=[2,3,4,5,8,4,3,5,2,1,8,8,6,3,4,5,7,9]
str1="hello python three"
l1u=set(l1)
l=len(l1u)
print("No. of unique elements:",l)
print("Odd numbers:")
for i in l1u:
    if i%2!=0:
        print(i, " ")
str=str1.replace("three","3")
print(str)
lst=str.upper().split()
print(lst)
