from typing import List

def quick_sort(elements:List) -> List:
    if len(elements) <= 1:
        return elements
    pivot = elements[0]
    lesser = [x for x in elements[1:] if x <= pivot]
    greater = [x for x in elements[1:] if x > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

elements = [58, 62, 91, 43, 29, 37, 88, 72, 16, 30]
print(quick_sort(elements))