#Find duplicate no in array
# Given an Array of , integers, return all elements that appear more than once
# example [1,2,3,4,2,4,5] o/p - 2,4
from collections import Counter

nums = [1,2,3,4,2,4]
# num= input("Enter randon no with seperate comma: ").strip().split(",")
# print(num)

def find_duplicate(nums):
    seen = set() # track number we have already visited
    duplicates = set() #Store confirmed duplicate (avoid re adding)
    for num in nums:
        if num in seen:  # Already visited → duplicate!
            duplicates.add(num)
        else:
            seen.add(num)   # First visit → mark as seen

    return list(duplicates)

print(find_duplicate(nums))
# print(find_duplicate(input("Enter no seperated with comma: ").strip().split(",")))


def find_duplicates_counter(nums):
    freq = Counter(nums) # {'2':2, '3':2, '1':1, ...}
    return [num for num,
            count in freq.items()
            if count>1]
print(find_duplicates_counter(nums))

