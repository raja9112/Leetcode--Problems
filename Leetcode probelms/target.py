# adding two elements in an array that must be eqaul to the given target and return the element's indices

def example(arr, target):
    n=len(arr)

    for i in range(n-1):
        for j in range(i+1, n):
            if(arr[i]+arr[j]==target):
                print(f"{[i,j]}")
        
inp=int(input("How many elements do you wish to add :"))
arr=[]
for x in range(inp):
    arr.append(int(input("Enter the number : ")))
tg=int(input("Enter a target number : "))

example(arr, tg)

