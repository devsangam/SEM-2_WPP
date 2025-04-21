import itertools
import random
import numpy as np
def find_combinations(n):
    numbers = range(1, n*n + 1)
    target = n * (n*n + 1) // 2  # The target sum S
    solutions = [comb for comb in itertools.combinations(numbers, n) if sum(comb) == target]
    return solutions

n=int(input("Enter a number:  "))
square=np.zeros((n,n))
possible_nums=[i for i in range(1,n*n+1)]

sols=np.array(find_combinations(n))
sols.flatten()
s_frequency=np.zeros(n*n+1 ,dtype=int)
center_values=[]#4
edge_values=[]#2
corner_values=[]#3
for s in sols:
    s_frequency[s]+=1
for i in range(n*n+1):
    if(s_frequency[i]==4):
        center_values.append(i)
    elif(s_frequency[i]==3):
        corner_values.append(i)
    elif(s_frequency[i]==2):
        edge_values.append(i)

if(n%2==0):
    center=[(n//2, n//2), (n//2-1, n//2), (n//2, n//2 -1), (n//2 -1, n//2 -1)]
else:
    center=[(n/2,n/2)]

coener=[(0,0), (0,n-1), (n-1,0), (n-1, n-1)]
#rest other are bulk
print(s_frequency)
print(sols)