from typing import List

def quick_sort(elements:List) -> List:
    if len(elements) <= 1:
        return elements
    
    pivot = 0
    left = 0
    right = len(elements)-1
    
    while left != right:
        if pivot < right:
            while elements[pivot] < elements[right]:
                right -= 1
            elements[pivot], elements[right] = elements[right], elements[pivot]
            pivot = right
            
        if pivot > left:
            while elements[pivot] > elements[left]:
                left += 1
            elements[pivot], elements[left] = elements[left], elements[pivot]
            pivot = left
    return quick_sort(elements[:pivot]) + [elements[pivot]] + quick_sort(elements[pivot+1:])

elements = [58, 62, 91, 43, 29, 37, 88, 72, 16, 30]
print(quick_sort(elements))