t=int(input())
results=[]
for i in range(t):
    string=list(input())
    if(len(string))==0:
        results.append("no answer")
        continue
    i=len(string)-2
    while i>=0 and string[i]>=string[i+1]:
        i-=1
    if i== -1:
        results.append("no answer")
        continue
    j=len(string)-1
    while string[j]<=string[i]:
        j-=1
    string[i], string[j] = string[j], string[i]
    string = string[:i+1] + string[i+1:][::-1]
    results.append("".join(string))
for result in results:
    print(result)