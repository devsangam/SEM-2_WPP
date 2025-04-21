n=int(input())
lst=[]
for i in range(n):
    number=int(input())
    num=number
    count=0
    while num:
        if number%(num%10)==0:
            count+=1
        num=num//10
    lst.append(count)
for item in lst:
    print(item)

"""n=int(input())
lst=[]
for i in range(n):
    n=int(input())
    count=0
    for j in str(n):
        if(n%int(j) == 0):
            count+=1
    lst.append(count)
for item in lst:
    print(item)"""


