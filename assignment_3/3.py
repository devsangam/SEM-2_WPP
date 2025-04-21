n=int(input())
lst=[]
for i in range(n):
    num=int(input())
    if num>2:
        if num%2==0:
            lst.append(2**(num//2) +2**(num//2-1)+1)
        else:
            lst.append(2**((num+1)//2) +2**((num+1)//2-1))
    else:
        if num==0: lst.append(1)
        elif num==1: lst.append(1*2)
for i in range(n):
    print(lst[i])