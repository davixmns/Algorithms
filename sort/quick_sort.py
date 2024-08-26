import random

def quick_sort(array):
    if(len(array) <= 1):
        return array
    else:    
        pivot = array[random.randint(0, len(array) - 1)]
        left = [i for i in array if i < pivot]
        right = [i for i in array if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)