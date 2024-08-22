from datetime import datetime
import random
from search.binary_search import binary_search
from sort.merge_sort import merge_sort

def execute_sort(func, arr):
    start = datetime.now()
    result = func(arr)
    end = datetime.now()
    execution_time = (end - start).total_seconds() * 1000
    print(f"{func.__name__}: {execution_time:.3f}ms")
    return result

def execute_search(func, arr, target):
    start = datetime.now()
    result = func(arr, target)
    end = datetime.now()
    execution_time = (end - start).total_seconds() * 1000
    print(f"{func.__name__}: {execution_time:.3f}ms")
    return result


max = 100
sorted_numbers = [i for i in range(1, max)]
random_numbers = [random.randint(1, max) for i in range(1, max)]
random_number = random.randint(1, max)

execute_sort(merge_sort, random_numbers)
execute_search(binary_search, sorted_numbers, random_number)
