import random
import math
import numpy as np
import matplotlib.pyplot as plt
def f(p, func):
    return sum(coef * math.pow(p, power) for coef, power in func)
def find_root(a, b ,x, y, func, min_diff=0.00000001):
    c=(a+b)/2
    fc = f(c, func)
    if(abs(b-a)<min_diff):
        plt.plot(x,y)
        plt.show()
        print("Approximate root is:",c)
    elif(f(a,func)*fc<0):
        x=np.append(x,a)
        y=np.append(y,c)
        return find_root(a,c,x, y, func ,min_diff)
    elif(f(b,func)*fc<0):
        x=np.append(x,c)
        y=np.append(y,b)
        return find_root(c,b,x, y, func, min_diff)
    else:
        print( "Root Not Found")

n=int(input("enter number of terms:\t"))
func=[]
for i in range(n):
    func.append((float(input("Coeffecient:\t")), float(input("Power:\t"))))
a=random.randint(-100, 100)
b=random.randint(-100, 100)
x=np.array([])
y=np.array([])
while(f(a, func)*f(b, func)>0):
    a=random.randint(-100, 100)
    b=random.randint(-100, 100)
    x=np.append(x,a)
    y=np.append(y,b)
plt.plot(x,y)
plt.show()
find_root(a,b,x,y,func)
