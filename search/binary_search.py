def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (right + left) // 2

        if array[mid] == target:
            return mid

        if target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_recursive(array, target, left, right):
    if left > right:
        return -1

    mid = (right + left) // 2

    if array[mid] == target:
        return mid

    if target < array[mid]:
        return binary_search_recursive(array, target, left, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, right)


input = ["ana", "bob", "carl", "dave", "ed", "frank", "gus", "hank", "ian", "joeeeee"]

print(binary_search_recursive(input, "ian", 0, len(input) - 1))