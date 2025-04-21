def digital_root(num):
    res=0
    while(num):
        res+=num%10
        num=num//10
    if(res<10):
        return res
    return digital_root(res)
print("Digital root of number is:\t", digital_root(int(input("Enter number:\t"))))