import random as r
lst=[r.randrange(0,2) for i in range(100)]
max_c, curr_count=0,0
for i in lst:
    if i:
        curr_count=0
    else:
        curr_count+=1
        if(curr_count>max_c):
            max_c=curr_count
print(lst)
print(max_c)