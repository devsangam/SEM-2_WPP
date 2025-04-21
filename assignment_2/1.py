str_i=input("Enter word:\t")
res= "".join(i+j for i,j in zip(str_i[::2].lower(),str_i[1::2].upper()))
print(res)
