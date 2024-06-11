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