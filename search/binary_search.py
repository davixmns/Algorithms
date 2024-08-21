def binary_search(array, target):
    return binary_search_recursive(array, target, 0, len(array) - 1)

def binary_search_recursive(array, target, left, right):
        if(left > right):
            return -1
        
        mid = left + (right - left) // 2

        if(array[mid] == target):
            return mid
        
        if(target < array[mid]):
            return binary_search_recursive(array, target, left, mid - 1)
        else:
            return binary_search_recursive(array, target, mid + 1, right)


numbers = [i for i in range(1, 10)]

print(binary_search(numbers, 9))