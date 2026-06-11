def linear_Search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=int(input().split())
target=int(input())
result=linear_Search(arr,target)
if result==-1:
    print("Element not found in the array.")
else:
    print(f"Element found at index: {result}")
    