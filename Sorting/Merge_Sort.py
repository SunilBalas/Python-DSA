from typing import List

def merge_sort(elements: List) -> List:
    if len(elements) > 1:
        mid = len(elements) // 2
        left_list = elements[:mid]
        right_list = elements[mid:]
        
        merge_sort(left_list)
        merge_sort(right_list)
        
        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                elements[k] = left_list[i]
                i += 1
            else:
                elements[k] = right_list[j]
                j += 1
            k += 1
            
        while i < len(left_list):
            elements[k] = left_list[i]
            i += 1
            k += 1
            
        while j < len(right_list):
            elements[k] = right_list[j]
            j += 1
            k += 1
            
    return elements
        
elements = [8, 2, -3, 4, 90, 18, -1]
print(merge_sort(elements))