"""
Created on Wed Mar  8 19:20:40 2023

@author: ghild
"""

#sorting an array 

#BUBBLE SORT
"""
simple but not efficient
Time complexity: O(n2)
Space complexity:O(1)
"""
def bubble_sort(elements):
    size=len(elements)
    
    for i in range(size-1):
        for j in range(size-i-1):
            if elements[j]>elements[j+1]:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
                


if __name__== '__main__':
    elements=[3,78,12,34,1,0,56]
    
    bubble_sort(elements)
    print(elements)
    
    
  
#SELECTION SORT

    
def selection_sort(arr):
    size=len(arr)
    
    for i in range(size):
        min_index=i
        for j in range(min_index+1,size):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
            
        
    
if __name__== '__main__':
    elements=[20,3,56,78,7]
    selection_sort(elements)
    print(elements)
    elements=[3,78,12,34,1,0,56]
    
    selection_sort(elements)
    print(elements)
    
