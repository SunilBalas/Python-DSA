from typing import List

def modified_bubble_sort(elements:List) -> None:
    n = len(elements)
    for i in range(1, n):
        sort_flag = False
        for j in range(n-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                sort_flag = True
        if not sort_flag:
            break

elements = [24, 58, 11, 67, 92, 43]
modified_bubble_sort(elements)
print(elements)