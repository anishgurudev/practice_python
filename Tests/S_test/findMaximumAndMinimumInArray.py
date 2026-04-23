#Logic: Python has built-in functions that directly return the min and max.
arr = [3, 5, 4, 1, 9]

def find_min_max(arr):
    return min(arr), max(arr)
minimum, maximum = find_min_max(arr)
print(f'minimum : {minimum}, \nmaximum: {maximum}')

def find_min_maxm(nums):
    if not nums:
        return None,None
    return min(arr),max(arr)

minimum, maximum = find_min_maxm(arr)
print(f'Minimum : {minimum} at index {arr.index(minimum)}, \nMaximum: {maximum} is at index {arr.index(maximum)}')

def find_min_max_sort(arr):
    sorted_arr =sorted(arr)
    return sorted_arr[0], sorted_arr[-1]
minimum, maximum = find_min_max_sort(arr)
print(f'minimum : {minimum}, \nmaximum: {maximum}')

# Linear Search with a Loop ⭐ (Interview Favourite)
# Logic: Assume the first element is both min and max.
# Then loop through the rest — update min if a smaller number is found,
# update max if a larger number is found.

def find_min_max_linear(arr):
    min_val = arr[0]   # Assume first element is minimum
    max_val = arr[0]   # Assume first element is maximum

    for num in arr[1:]:      # Loop from 2nd element onwards
        if num < min_val:    # Found something smaller?
            min_val = num    # Update minimum
        if num > max_val:    # Found something larger?
            max_val = num    # Update maximum

    return min_val, max_val

minimum, maximum = find_min_max_linear(arr)
print(f'Minimum : {minimum} at index {arr.index(minimum)}, \nMaximum: {maximum} is at index {arr.index(maximum)}')
