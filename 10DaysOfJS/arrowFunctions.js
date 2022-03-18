/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    nums.forEach((element, index) => {
        element % 2 === 0 ? nums[index] = element * 2 : nums[index] = element * 3
    })
    // console.log(nums)
    return nums
}

let nums = [1,2,3,4,5]
modifyArray(nums)