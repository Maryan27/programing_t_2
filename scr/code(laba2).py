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
            
    return result

def find_three_numbers(array, target):
    array = merge_sort(array)
    n = len(array)
    for i in range(n - 2):
        second = i + 1
        last = n - 1
        while second < last:
            current_sum = array[i] + array[second] + array[last]
            if current_sum == target:
                return True
            elif current_sum < target:
                second += 1
            else:
                last -= 1
    return False
