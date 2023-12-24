from typing import List

def selection_sort(elements:List) -> None:
    n = len(elements)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if elements[min] > elements[j]:
                min = j
        elements[i], elements[min] = elements[min], elements[i]

elements = [24, 58, 11, 67, 92, 43]
selection_sort(elements)
print(elements)