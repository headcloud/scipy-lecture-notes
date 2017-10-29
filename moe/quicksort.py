# coding: utf-8
def quicksort(inp):
    array = inp
    print("input: ", array)
    if len(array) < 2:
        return array
    
    pivot_index = len(array) // 2
    pivot = array.pop(pivot_index)
    print("pivot: ",  pivot)
    
    less = []
    greater = []
    for x in array:
        if x < pivot + 1:
            less.append(x)
        else:
            greater.append(x)
    
    print("less: ", less)
    print("greater: ", greater)
    
    result = quicksort(less) + [pivot] + quicksort(greater)
    
    print("intermediate result: ", result)
    return result
