n=9
for i in range(1,2*n):
    for j in range(1,2*n):
        if(j<=i and j<=(2*n-i)):
            print("*",end="")
        elif(j>=i and j>=(2*n-i)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
 
for i in range(1,n):
    for j in range(2*n-1):
        if j<i:
            print(" ",end="")
        else:
            print("*",end="")
    print()
