l=int(input())
r=int(input())
answer=0
for i in range(l,r+1):
    for j in range(i, r+1):
        answer = answer if (i^j)<answer else (i^j)
print(answer)