eq_class0 = []
eq_class1 = []
eq_class2 = []
eq_class3 = []
eq_class4 = []
for i in range (1001):
    if i%5==0: 
        eq_class0.append(i)
    elif i%5==1: 
        eq_class1.append(i)
    elif i%5==2: 
        eq_class2.append(i)
    elif i%5==3: 
        eq_class3.append(i)
    else: 
        eq_class4.append(i)
print(eq_class0)
print(eq_class1)
print(eq_class2)
print(eq_class3)
print(eq_class4)
