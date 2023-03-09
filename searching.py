"""
Created on Thu Mar  9 07:57:00 2023

@author: ghild
"""

# SERACHING


# Linear search
def linear_search(arr, search):
    for i in range(len(arr)):
        if arr[i] == search:
            
            return i
    return -1              

# binary search
def binary_search(arr, search):
    l = 0
    u = len(arr)
    while l <= u:
        mid = (l+u)//2
        if arr[mid] < search:
            l = mid+1

        elif arr[mid] > search:
            
                u = mid-1
        else:
            return mid

    return -1      



# taking input list from user

# creating empty list
arr = []
# number of elements in list
n = int(input("Enter the number of elements you want in the list"))
# adding elements
for i in range(0, n):
    element = int(input())
    arr.append(element)
print(arr, " ")

search = int(input("enter the number you want to search"))
choice = int(input("enter 1 for linear search and 2 for binary search"))
if choice == 1:
    result= linear_search(arr, search)
    if result != -1:
       print("Element found at index", str(result))
    else: 
       print("Element is not present in array")
elif choice == 2:
    result=binary_search(arr, search)
    if result != -1:
        print("Element is not found at index")
    else: 
        print("Element is present in array")
else:
    print("invalid number")
