def isFibo(n, f1=0,f2=1):
    fib=f1+f2
    if n==fib:
        return True
    elif n>fib:
        return isFibo(n,f2,fib)
    return False
n=int(input())
lst=[]
for i in range(n):
    num=int(input())
    lst.append('IsFibo' if isFibo(num) else 'IsNotFibo')
for i in range(n):
    print(lst[i])