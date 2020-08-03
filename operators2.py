num_list=[int(x) for x in input().split()]
res=0
for i in num_list:
    res=res^i
print(num_list)
print(res)
