//// Two Sum

// O(n)
function twoSum(nums, target){
    for (const i of nums) {
        diff = target - i
        if (nums.includes(diff)) {
            return [nums.indexOf(i), nums.indexOf(diff)]
        }
    }
}