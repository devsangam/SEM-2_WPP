n=int(input("Enter number of students:\t"))
lst=[]
for i in range(n):
    name=input("Enter Name:\t")
    lst.append(name[:15:][::-1])
print(lst)