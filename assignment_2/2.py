products={}
while(1):
    prod=input("Enter in the format: 'product,price'\n press 0 to exit:\t")
    if(prod !='0'):
        prod=prod.split(",")
        products[prod[0]]=prod[1]
    else:
        break
while(1):
    prod=input("Enter prodict to search or enter 0 to search:\t")
    if(prod=='0'):
        break
    elif(prod in products.keys()):
        print("Price is:", products[prod])
    else:
        print("Product not found")