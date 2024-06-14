## Two Sum

# O(n²)
def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# O(n)
def two_sum(nums: list, target: int) -> list:
    for i in nums:
        diff = target - i
        if diff in nums:
            return [nums.index(i), nums.index(diff)]


## Valid Parentheses

# O(n²)
def isValid_parentheses(s: str) -> bool:
    while '[]' in s or '{}' in s or '()' in s:
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    return not s
    
## Merge Two Sorted Lists

# O(1)
merge_two_sorted_lists = lambda list1, list2 : sorted(list1+list2)