# LEVEL : EASY
#Question : Two sum

#To get the index of elements which are equal to given target when adding the element with another element

def twosum(arr, target):
    n=len(arr)

    for i in range(n-1):
        for j in range(i+1, n):
            if (arr[i]+arr[j] == target):
                print([i,j])



get=int(input("How many elements do you want to add : "))
arr=[]
for i in range(get):
    arr.append(int(input("Enter the number : ")))

target=int(input("\nEnter the target : "))

print(arr)
twosum(arr,target)
