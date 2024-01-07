from typing import List

def insertion_sort(elements:list) -> None:
    n = len(elements)
    for i in range(1, n):
        temp = elements[i]
        
        j = i-1
        while j >= 0 and temp < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = temp

elements = [20, 50, 63, 19, 8, -2, 98]
insertion_sort(elements)
print(elements)