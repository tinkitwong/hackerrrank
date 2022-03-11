function getSecondLargest(nums) {
    // Complete the function
    
    // create array of unique elements
    nums = Array.from(new Set(nums))
    // sort in ascending order 
    nums.sort(function(a,b) {return a-b})
    return nums[nums.length -2]
}

nums = [2,3,6,6,5]
getSecondLargest(nums)