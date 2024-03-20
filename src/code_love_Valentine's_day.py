def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    left_pos, right_pos = 0, 0
    
    while left_pos < len(left) and right_pos < len(right):
        if left[left_pos] < right[right_pos]:
            result.append(left[left_pos])
            left_pos += 1
        else:
            result.append(right[right_pos])
            right_pos += 1

    result.extend(left[left_pos:])
    result.extend(right[right_pos:])
            
    return result

def binary_search(array, second, last, target):
    while second <= last:
        mid = (second + last) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            second = mid + 1
        else:
            last = mid - 1
    return False

def find_three_numbers(array, target):
    array = merge_sort(array)
    n = len(array)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            current_sum = target - (array[i] + array[j])
            if binary_search(array, j + 1, n - 1, current_sum):
                return True
    return False


