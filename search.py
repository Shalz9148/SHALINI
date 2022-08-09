def search(l,key):
    for i in range(len(l)):
        if l[i]==key:
            return i
    return -1
#main function
l=list()
N=int(input("enter the number of elements you want to enter:"))
for i in range(N):
    E=int(input("enter the number:"))
    l.append(E)
print(l)
          
key=int(input("enter the of element you want to search:"))
found=search(l,key)
if found== -1:
    print("the key not found")
else:
    print("the key found in position of",found)
