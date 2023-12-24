from typing import List

def bubble_sort(elements:List) -> None:
    n = len(elements)
    for i in range(1, n):
        for j in range(n-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

elements = [10, 5, -2, 0, 1, 98, 72, 65]
bubble_sort(elements)
print(elements)