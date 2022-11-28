def input_matrix():
    for i in range(1,row+1):
        r = []
        for j in range(1,col+1):
            print("Enter Number of Coloumn #",j,",Row #",i," : ",end="")
            n=input()
            r.append(n)
        mat.append(r)

    for e in mat:
        for num in e:
            print(num,end=" ")
        print()

mat=[]
col = int(input("Enter Number of coloums : "))
row = int(input("Enter number of rows : "))
print(input_matrix())
