from math import sqrt
import sys
def dist(point1,point2):
    distance=sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)
    return distance
lst=[]
min_dist_lst=[]
for i in range(10):
    n=input("Enter coordinates in the format 'x,y,z'\t").split(',')
    n=[float(n[i]) for i in range(len(n))]
    lst.append(n)
    index=None
for i in range(10):
    min_dist=sys.maxsize
    for j in range(10):
        distance=dist(lst[i], lst[j])
        if(i==j):
            continue
        elif(min_dist>distance):
            min_dist=distance
            index=j   
    min_dist_lst.append(lst[index])        
print(min_dist_lst)